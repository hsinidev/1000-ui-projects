import os
import json
import re
import shutil

# Paths
BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"
OUTPUT_TXT = r"C:\Users\hsini\.gemini\antigravity\brain\b275222c-1cc5-4d8d-8d8c-c011b7de24c0\.system_generated\steps\4\output.txt"

def slugify(text):
    return re.sub(r'[\W_]+', '_', text).lower().strip('_')

def load_all_metadata():
    print("Loading metadata from output.txt...")
    with open(OUTPUT_TXT, "r", encoding="utf-8") as f:
        content = f.read()
    
    # The output.txt seems to be a JSON with a 'projects' key at the end
    # Let's find the start of the projects list
    start_idx = content.find('"projects":')
    if start_idx == -1:
        # Try a different approach: find all { "name": "projects/..." }
        print("Could not find 'projects' key, using fallback extraction...")
        project_blocks = re.findall(r'\{[^{}]*"name":\s*"projects/\d+"[^{}]*"title":\s*"[^"]+"[^{}]*\}', content)
        projects = []
        for block in project_blocks:
            try:
                projects.append(json.loads(block))
            except:
                pass
    else:
        # Extract everything from '"projects": [' to the end
        list_start = content.find('[', start_idx)
        list_end = content.rfind(']') + 1
        try:
            projects = json.loads(content[list_start:list_end])
        except:
            print("Failed to parse projects list JSON.")
            projects = []
    
    print(f"Loaded {len(projects)} project definitions.")
    
    mapping = {}
    for p in projects:
        title = p.get("title", "")
        slug = slugify(title)
        mapping[slug] = p
        # Also map variations
        mapping[f"stitch_{slug}"] = p
    
    return mapping

def build_portal(folder_name, project_data):
    project_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(project_path):
        return

    # 1. Identify screens
    # Case A: Nested screen folders (Standard)
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder):
        inner_folder = project_path
    
    screens = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d)) and d != folder_name]
    screen_links = []
    
    for screen in screens:
        code_path = os.path.join(inner_folder, screen, "code.html")
        if os.path.exists(code_path):
            dest_path = os.path.join(project_path, f"{screen}.html")
            shutil.copy(code_path, dest_path)
            screen_links.append({
                "name": screen.replace("_", " ").title(),
                "file": f"{screen}.html"
            })
    
    # Case B: Single screen code.html in root
    root_code = os.path.join(project_path, "code.html")
    if os.path.exists(root_code) and not screen_links:
        dest_path = os.path.join(project_path, "main_screen.html")
        shutil.copy(root_code, dest_path)
        screen_links.append({
            "name": "Main Screen",
            "file": "main_screen.html"
        })
    
    if not screen_links:
        print(f"No screens found for {folder_name}")
        return

    # 2. Extract Metadata for Theme
    title = project_data.get("title", folder_name.replace("stitch_", "").replace("_", " ").title())
    theme = project_data.get("designTheme", {})
    colors = theme.get("colors", {})
    
    # 3. Generate index.html (Premium Portal)
    primary = colors.get("primary", "#3b82f6")
    bg = colors.get("background", "#0f172a")
    on_bg = colors.get("onBackground", "#f8fafc")
    surface = colors.get("surface", "rgba(255,255,255,0.05)")
    
    links_html = "".join([f"""
        <li>
            <a href="{l["file"]}" class="group block p-6 bg-white/5 hover:bg-white/10 border border-white/10 rounded-2xl transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">
                <div class="flex justify-between items-center">
                    <span class="text-xl font-semibold tracking-tight group-hover:text-[{primary}] transition-colors">{l["name"]}</span>
                    <svg class="w-6 h-6 opacity-0 group-hover:opacity-100 transition-all -translate-x-4 group-hover:translate-x-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                    </svg>
                </div>
            </a>
        </li>
    """ for l in screen_links])
    
    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Design System Explorer</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: {bg};
            color: {on_bg};
            font-family: 'Inter', sans-serif;
            background-image: radial-gradient(circle at 50% -20%, {primary}22, transparent 50%);
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
    </style>
</head>
<body class="min-h-screen py-20 px-6">
    <div class="max-w-3xl mx-auto">
        <header class="mb-16 text-center">
            <div class="inline-block px-4 py-1.5 mb-6 rounded-full bg-white/5 border border-white/10 text-[10px] font-bold tracking-[0.2em] uppercase text-white/50">
                Stitch UI Portfolio
            </div>
            <h1 class="text-5xl md:text-6xl font-800 tracking-tighter mb-4" style="color: {primary}">{title}</h1>
            <p class="text-lg text-white/40 max-w-xl mx-auto">Explore the interactive high-fidelity screens designed for this experience.</p>
        </header>
        
        <nav>
            <ul class="grid grid-cols-1 gap-4">
                {links_html}
            </ul>
        </nav>
        
        <footer class="mt-20 pt-10 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6 text-white/30 text-xs font-medium uppercase tracking-widest">
            <div>&copy; 2026 Stitch Design System</div>
            <div class="flex gap-8">
                <a href="#" class="hover:text-white transition-colors">Documentation</a>
                <a href="#" class="hover:text-white transition-colors">Design Specs</a>
                <a href="#" class="hover:text-white transition-colors">Project Info</a>
            </div>
        </footer>
    </div>
</body>
</html>"""

    with open(os.path.join(project_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"DONE Portal built: {title}")

def main():
    mapping = load_all_metadata()
    
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    
    for folder in folders:
        # Find project data
        # Try exact match, then slug match
        project_data = mapping.get(folder)
        if not project_data:
            # Try to find by normalized name
            slug = slugify(folder.replace("stitch_", ""))
            project_data = mapping.get(slug)
        
        if project_data:
            build_portal(folder, project_data)
        else:
            # Minimal fallback if no metadata found
            build_portal(folder, {})

if __name__ == "__main__":
    main()
