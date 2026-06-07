import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

def find_home_screen(screens):
    priorities = ["home", "dashboard", "index", "main", "portal", "landing", "overview"]
    for p in priorities:
        for screen in screens:
            if p in screen.lower():
                return screen
    return screens[0] if screens else None

def smart_link(html_content, screens_map):
    # screens_map: { "folder_name": "target_filename.html" }
    
    # 1. First, replace known patterns like folder.html
    for folder, target in screens_map.items():
        html_content = html_content.replace(f'href="{folder}.html"', f'href="{target}"')
        html_content = html_content.replace(f'href="./{folder}.html"', f'href="{target}"')

    # 2. Smart text matching for <a> tags with href="#"
    # Regex to find <a ... href="#" ...>Text</a>
    pattern = re.compile(r'(<a\s+[^>]*href=["\']#["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    
    def replace_link(match):
        prefix, text, suffix = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip().lower()
        if not clean_text:
            return match.group(0)
            
        # Try to find a match in screens_map
        best_match = None
        for folder, target in screens_map.items():
            folder_clean = folder.lower().replace("_", " ")
            # Check if text is in folder name or vice versa
            if clean_text in folder_clean or folder_clean in clean_text:
                best_match = target
                break
                
        if best_match:
            new_prefix = prefix.replace('href="#"', f'href="{best_match}"')
            return f"{new_prefix}{text}{suffix}"
        
        return match.group(0)

    return pattern.sub(replace_link, html_content)

def process_project(folder_name):
    project_path = os.path.join(BASE_DIR, folder_name)
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder):
        inner_folder = project_path
    
    screen_dirs = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d)) and d != folder_name]
    
    if not screen_dirs:
        root_code = os.path.join(project_path, "code.html")
        if os.path.exists(root_code):
            shutil.copy(root_code, os.path.join(project_path, "index.html"))
        return

    home_screen = find_home_screen(screen_dirs)
    
    screens_map = {}
    for d in screen_dirs:
        if d == home_screen:
            screens_map[d] = "index.html"
        else:
            screens_map[d] = f"{d}.html"

    for d in screen_dirs:
        code_path = os.path.join(inner_folder, d, "code.html")
        if os.path.exists(code_path):
            with open(code_path, "r", encoding="utf-8") as f:
                html = f.read()
            
            fixed_html = smart_link(html, screens_map)
            
            target_filename = screens_map[d]
            target_path = os.path.join(project_path, target_filename)
            
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(fixed_html)
            
            if d == home_screen:
                shutil.copy(target_path, os.path.join(project_path, f"{d}.html"))

    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        process_project(f)
