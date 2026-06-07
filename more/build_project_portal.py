import os
import json
import re
import shutil

# Paths
BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"
OUTPUT_TXT = r"C:\Users\hsini\.gemini\antigravity\brain\b275222c-1cc5-4d8d-8d8c-c011b7de24c0\.system_generated\steps\4\output.txt"

def get_project_metadata(slug):
    with open(OUTPUT_TXT, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Map slug to title
    # Slug is like 'boutique_luxury_hotel_ui'
    # Title is like 'Boutique Luxury Hotel UI'
    expected_title = slug.replace("stitch_", "").replace("_", " ").title()
    if "Ui" in expected_title: expected_title = expected_title.replace("Ui", "UI")
    
    # Search for project with this title
    # Pattern: "name": "projects/(\d+)", "title": "TITLE"
    match = re.search(r'\{[^{}]*"title":\s*"' + re.escape(expected_title) + r'"[^{}]*\}', content)
    if not match:
        # Try finding by ID if possible, but let's try searching titles first
        return None
    
    # Extract the whole block
    start_idx = match.start()
    brace_count = 0
    obj_start = content.rfind('{', 0, start_idx + 1)
    obj_end = -1
    for i in range(obj_start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                obj_end = i + 1
                break
    
    if obj_end == -1: return None
    
    try:
        return json.loads(content[obj_start:obj_end])
    except:
        return None

def build_portal(folder_name):
    project_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(project_path):
        print(f"Folder {folder_name} not found.")
        return

    # 1. Identify screens
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder):
        print(f"Inner folder {inner_folder} not found.")
        return
    
    screens = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d))]
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
    
    # 2. Get Metadata for Theme
    meta = get_project_metadata(folder_name)
    title = meta.get("title", folder_name.replace("stitch_", "").replace("_", " ").title())
    colors = meta.get("designTheme", {}).get("colors", {})
    
    # 3. Generate index.html
    # We'll use a premium template similar to the telemetry one
    primary_color = colors.get("primary", "#3b82f6")
    bg_color = colors.get("background", "#0f172a")
    on_bg = colors.get("onBackground", "#f8fafc")
    
    links_html = "".join([f'<li><a href="{l["file"]}" class="block p-4 bg-white/5 hover:bg-white/10 border border-white/10 rounded-lg transition-all hover:translate-x-2 text-lg font-medium">{l["name"]}</a></li>' for l in screen_links])
    
    index_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: {bg_color};
            color: {on_bg};
            font-family: 'Inter', sans-serif;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6">
    <div class="max-w-2xl w-full glass p-8 rounded-2xl shadow-2xl">
        <header class="mb-8 text-center">
            <h1 class="text-4xl font-800 tracking-tight mb-2" style="color: {primary_color}">{title}</h1>
            <p class="text-white/60 uppercase tracking-widest text-sm font-semibold">Project Screen Portal</p>
        </header>
        
        <nav>
            <ul class="space-y-4">
                {links_html}
            </ul>
        </nav>
        
        <footer class="mt-12 pt-8 border-t border-white/10 text-center text-white/40 text-sm">
            &copy; 2026 Stitch Design System • Professional UI Export
        </footer>
    </div>
</body>
</html>"""

    with open(os.path.join(project_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"Portal built for {title} with {len(screen_links)} screens.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        build_portal(sys.argv[1])
    else:
        print("Provide folder name.")
