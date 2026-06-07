# publish_to_github.ps1
# Publishes all stitch_ projects to GitHub under hsinidev
# Repo name = project folder name with "stitch_" prefix removed
# Usage: .\publish_to_github.ps1
# Optional: .\publish_to_github.ps1 -StartFrom 50 -BatchSize 100

param(
    [int]$StartFrom = 0,       # Skip the first N projects (for resuming)
    [int]$BatchSize = 880,     # How many to process in this run
    [switch]$DryRun = $false   # Set -DryRun to preview without creating repos
)

$ErrorActionPreference = "Continue"
$RootDir = Split-Path -Parent $PSScriptRoot
$GithubUser = "hsinidev"
$LogFile = "$PSScriptRoot\publish_log.txt"
$FailedLog = "$PSScriptRoot\failed_repos.txt"

# Clear logs if starting fresh
if ($StartFrom -eq 0) {
    "" | Set-Content $LogFile
    "" | Set-Content $FailedLog
}

function Log($msg) {
    $ts = Get-Date -Format "HH:mm:ss"
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content $LogFile $line
}

# Collect all top-level stitch_ projects from every category folder
$AllProjects = @()
Get-ChildItem -Path $RootDir -Directory | ForEach-Object {
    $category = $_
    Get-ChildItem -Path $category.FullName -Directory -Filter "stitch_*" | ForEach-Object {
        $AllProjects += [PSCustomObject]@{
            Category    = $category.Name
            ProjectDir  = $_.FullName
            StitchName  = $_.Name
            RepoName    = $_.Name -replace '^stitch_', ''
        }
    }
}

$Total = $AllProjects.Count
Log "Found $Total total projects. Processing from index $StartFrom, batch size $BatchSize"

$Batch = $AllProjects | Select-Object -Skip $StartFrom -First $BatchSize
$Success = 0
$Failed  = 0
$Skipped = 0
$idx     = $StartFrom

foreach ($proj in $Batch) {
    $idx++
    $repoName = $proj.RepoName
    $projDir  = $proj.ProjectDir

    Log "[$idx/$Total] $repoName  ($($proj.Category))"

    if ($DryRun) {
        Log "  [DRY RUN] Would create: https://github.com/$GithubUser/$repoName"
        $Success++
        continue
    }

    # ----- Step 1: Check if repo already exists -----
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

    # ----- Step 5: Create GitHub repo -----
    $createOutput = gh repo create "$GithubUser/$repoName" --public --source "$projDir" --remote origin --push 2>&1
    if ($LASTEXITCODE -eq 0) {
        Log "  [OK] https://github.com/$GithubUser/$repoName"
        $Success++
    } else {
        # Try just pushing if repo create partially succeeded
        Push-Location $projDir
        $pushOutput = git push -u origin main 2>&1
        if ($LASTEXITCODE -eq 0) {
            Log "  [OK-PUSH] https://github.com/$GithubUser/$repoName"
            $Success++
        } else {
            Log "  [FAIL] $repoName -- $createOutput"
            Add-Content $FailedLog "$repoName`t$projDir"
            $Failed++
        }
        Pop-Location
    }

    # Small delay to respect GitHub rate limits (avoid 429 errors)
    Start-Sleep -Milliseconds 500
}

Log ""
Log "===== DONE ====="
Log "Success : $Success"
Log "Skipped : $Skipped (already existed)"
Log "Failed  : $Failed"
Log "Log     : $LogFile"
if ($Failed -gt 0) {
    Log "Failed repos saved to: $FailedLog"
}
