# retry_publish.ps1
# Publishes all stitch_ projects to GitHub under hsinidev, skipping existing ones.
# Handles rate limits by sleeping.
# Usage: .\retry_publish.ps1

$ErrorActionPreference = "Continue"
$RootDir = Split-Path -Parent $PSScriptRoot
$GithubUser = "hsinidev"
$LogFile = "$PSScriptRoot\retry_publish_log.txt"
$FailedLog = "$PSScriptRoot\retry_failed_repos.txt"

function Log($msg) {
    $ts = Get-Date -Format "HH:mm:ss"
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content $LogFile $line
}

# Collect all top-level stitch_ projects
$AllProjects = @()
Get-ChildItem -Path $RootDir -Directory | ForEach-Object {
    $category = $_
    Get-ChildItem -Path $category.FullName -Directory -Filter "stitch_*" | ForEach-Object {
        $AllProjects += [PSCustomObject]@{
            Category    = $category.Name
            ProjectDir  = $_.FullName
            RepoName    = $_.Name -replace '^stitch_', ''
        }
    }
}

$Total = $AllProjects.Count
Log "Found $Total total projects. Resuming publish..."

$Success = 0
$Failed  = 0
$Skipped = 0
$idx     = 0

foreach ($proj in $AllProjects) {
    $idx++
    $repoName = $proj.RepoName
    $projDir  = $proj.ProjectDir

    Log "[$idx/$Total] $repoName"

    # ----- Step 1: Check if repo already exists -----
    # Using gh api to check repo existence is sometimes faster/more reliable
    $exists = gh repo view "$GithubUser/$repoName" --json name 2>$null
    if ($LASTEXITCODE -eq 0) {
        Log "  [SKIP] Repo already exists: https://github.com/$GithubUser/$repoName"
        $Skipped++
        continue
    }

    # ----- Step 2: Init git in the project folder -----
    if (-not (Test-Path "$projDir\.git")) {
        Push-Location $projDir
        git init -b main 2>&1 | Out-Null
        Pop-Location
    }

    # ----- Step 3: Add README if none exists -----
    if (-not (Test-Path "$projDir\README.md")) {
        $readmeContent = "# $repoName`n`n> Part of the 1000 Stitch UI Projects collection.`n`nCategory: **$($proj.Category)**`n"
        Set-Content "$projDir\README.md" $readmeContent -Encoding UTF8
    }

    # ----- Step 4: Stage & commit -----
    Push-Location $projDir
    git add -A 2>&1 | Out-Null
    $status = git status --porcelain 2>&1
    if ($status) {
        git commit -m "Initial commit: $repoName" 2>&1 | Out-Null
    }
    Pop-Location

    # ----- Step 5: Create GitHub repo with Retry -----
    $retryCount = 0
    $created = $false

    while (-not $created -and $retryCount -lt 3) {
        $createOutput = gh repo create "$GithubUser/$repoName" --public --source "$projDir" --remote origin --push 2>&1
        
        if ($LASTEXITCODE -eq 0) {
            Log "  [OK] https://github.com/$GithubUser/$repoName"
            $Success++
            $created = $true
        } else {
            if ($createOutput -match "too many repositories, too quickly") {
                Log "  [RATE LIMIT] Hit rate limit. Sleeping for 120 seconds before retry..."
                Start-Sleep -Seconds 120
                $retryCount++
            } else {
                # Try just pushing if repo create partially succeeded
                Push-Location $projDir
                $pushOutput = git push -u origin main 2>&1
                if ($LASTEXITCODE -eq 0) {
                    Log "  [OK-PUSH] https://github.com/$GithubUser/$repoName"
                    $Success++
                    $created = $true
                } else {
                    Log "  [FAIL] $repoName -- $createOutput"
                    Add-Content $FailedLog "$repoName`t$projDir"
                    $Failed++
                    break
                }
                Pop-Location
            }
        }
    }
    
    if (-not $created -and $retryCount -ge 3) {
        Log "  [FAIL] $repoName -- Failed after 3 retries due to rate limiting."
        Add-Content $FailedLog "$repoName`t$projDir"
        $Failed++
    }

    # Delay between requests to avoid hitting limits again
    Start-Sleep -Seconds 3
}

Log ""
Log "===== DONE ====="
Log "Success : $Success"
Log "Skipped : $Skipped (already existed)"
Log "Failed  : $Failed"
