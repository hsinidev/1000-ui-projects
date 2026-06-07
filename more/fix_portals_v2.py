import os
import json
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

def slugify(text):
    return re.sub(r'[\W_]+', '_', text).lower().strip('_')

def find_home_screen(screens):
    # Priority keywords for home screen
    priorities = ["home", "dashboard", "index", "main", "portal", "landing", "overview"]
    for p in priorities:
        for screen in screens:
            if p in screen.lower():
                return screen
    return screens[0] if screens else None

def fix_links(html_content, screens_map):
    # screens_map: { "folder_name": "target_filename.html" }
    
    # Also handle the Stitch-specific navigation patterns
    # Often they link to "folder_name.html" or "folder_name/code.html"
    
    # 1. Replace folder_name.html with target_filename.html
    fixed_html = html_content
    for folder, target in screens_map.items():
        # Replace instances of folder.html with target
        # e.g., href="gaming_hub_home.html" -> href="index.html"
        fixed_html = fixed_html.replace(f'href="{folder}.html"', f'href="{target}"')
        fixed_html = fixed_html.replace(f'href="./{folder}.html"', f'href="{target}"')
        
    return fixed_html

def process_project(folder_name):
    project_path = os.path.join(BASE_DIR, folder_name)
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder):
        inner_folder = project_path
    
    screen_dirs = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d)) and d != folder_name]
    
    if not screen_dirs:
        # Check for single code.html
        root_code = os.path.join(project_path, "code.html")
        if os.path.exists(root_code):
            shutil.copy(root_code, os.path.join(project_path, "index.html"))
            print(f"Single screen project: {folder_name}")
            return
        print(f"No screens found for {folder_name}")
        return

    home_screen = find_home_screen(screen_dirs)
    
    # Mapping of folder names to their new HTML filenames
    screens_map = {}
    for d in screen_dirs:
        if d == home_screen:
            screens_map[d] = "index.html"
        else:
            screens_map[d] = f"{d}.html"

    # Process each screen
    for d in screen_dirs:
        code_path = os.path.join(inner_folder, d, "code.html")
        if os.path.exists(code_path):
            with open(code_path, "r", encoding="utf-8") as f:
                html = f.read()
            
            # Fix links to point to the new flat structure
            fixed_html = fix_links(html, screens_map)
            
            target_filename = screens_map[d]
            target_path = os.path.join(project_path, target_filename)
            
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(fixed_html)
            
            # Also keep a copy with the original name for compatibility if it's index.html
            if d == home_screen:
                shutil.copy(target_path, os.path.join(project_path, f"{d}.html"))

    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_project(sys.argv[1])
    else:
        folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
        for f in folders:
            process_project(f)
