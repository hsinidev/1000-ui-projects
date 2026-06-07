import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

def find_home_screen(screens, inner_folder):
    valid_screens = []
    for s in screens:
        if os.path.exists(os.path.join(inner_folder, s, "code.html")):
            valid_screens.append(s)
            
    if not valid_screens:
        return None
        
    priorities = ["home", "dashboard", "index", "main", "portal", "landing", "overview", "selector"]
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower():
                return screen
    return valid_screens[0]

def smart_link(html_content, screens_map):
    for folder, target in screens_map.items():
        html_content = html_content.replace(f'href="{folder}.html"', f'href="{target}"')
        html_content = html_content.replace(f'href="./{folder}.html"', f'href="{target}"')

    pattern = re.compile(r'(<a\s+[^>]*href=["\']#["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    
    def replace_link(match):
        prefix, text, suffix = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip().lower()
        if not clean_text:
            return match.group(0)
            
        best_match = None
        for folder, target in screens_map.items():
            folder_clean = folder.lower().replace("_", " ")
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
    
    home_screen = find_home_screen(screen_dirs, inner_folder)
    
    if not home_screen:
        return

    screens_map = {}
    for d in screen_dirs:
        if os.path.exists(os.path.join(inner_folder, d, "code.html")):
            if d == home_screen:
                screens_map[d] = "index.html"
            else:
                screens_map[d] = f"{d}.html"

    for d, target_filename in screens_map.items():
        code_path = os.path.join(inner_folder, d, "code.html")
        with open(code_path, "r", encoding="utf-8") as f:
            html = f.read()
        
        fixed_html = smart_link(html, screens_map)
        target_path = os.path.join(project_path, target_filename)
        
        # This will overwrite any existing generic index.html
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(fixed_html)
        
        if d == home_screen:
            shutil.copy(target_path, os.path.join(project_path, f"{d}.html"))

    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        try:
            process_project(f)
        except Exception as e:
            print(f"Error processing {f}: {e}")
