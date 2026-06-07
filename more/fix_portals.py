import os
import json
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

def slugify(text):
    return re.sub(r'[\W_]+', '_', text).lower().strip('_')

def find_home_screen(screens):
    # Priority keywords
    priorities = ["home", "dashboard", "index", "main", "portal"]
    for p in priorities:
        for screen in screens:
            if p in screen.lower():
                return screen
    return screens[0] if screens else None

def fix_links(html_content, screens_map):
    # screens_map is a dict of { "label": "filename.html" }
    
    # Also add "Home" to map
    screens_map["home"] = "index.html"
    
    # Find all <a> tags with href="#"
    # We'll use regex to find tags and their content
    def replacer(match):
        full_tag = match.group(0)
        content = match.group(2)
        # Strip HTML tags from content for matching
        text_content = re.sub(r'<[^>]+>', '', content).strip().lower()
        
        for label, filename in screens_map.items():
            if label in text_content or text_content in label:
                return full_tag.replace('href="#"', f'href="{filename}"')
        
        return full_tag

    # Match <a ... href="#" ...>Content</a>
    # Note: This is a bit naive but should work for these standard exports
    fixed_html = re.sub(r'(<a\s+[^>]*href="#"[^>]*>)(.*?)(</a>)', replacer, html_content, flags=re.DOTALL | re.IGNORECASE)
    return fixed_html

def process_project(folder_name):
    project_path = os.path.join(BASE_DIR, folder_name)
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder):
        inner_folder = project_path
    
    screen_dirs = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d)) and d != folder_name]
    if not screen_dirs:
        # Check for single code.html
        if os.path.exists(os.path.join(project_path, "code.html")):
            shutil.copy(os.path.join(project_path, "code.html"), os.path.join(project_path, "index.html"))
            print(f"Single screen project: {folder_name}")
            return
        print(f"No screens found for {folder_name}")
        return

    # Map screen names to their target filenames
    screens_map = {}
    for d in screen_dirs:
        label = d.replace("_", " ").lower()
        screens_map[label] = f"{d}.html"
        # Also add parts of the label
        for part in label.split():
            if len(part) > 3: screens_map[part] = f"{d}.html"

    home_screen = find_home_screen(screen_dirs)
    
    for d in screen_dirs:
        code_path = os.path.join(inner_folder, d, "code.html")
        if os.path.exists(code_path):
            with open(code_path, "r", encoding="utf-8") as f:
                html = f.read()
            
            fixed_html = fix_links(html, screens_map)
            
            # Write to screen file
            with open(os.path.join(project_path, f"{d}.html"), "w", encoding="utf-8") as f:
                f.write(fixed_html)
            
            # If this is home, also write to index.html
            if d == home_screen:
                with open(os.path.join(project_path, "index.html"), "w", encoding="utf-8") as f:
                    f.write(fixed_html)

    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_project(sys.argv[1])
    else:
        # Process all stitch_* folders
        folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
        for f in folders:
            process_project(f)
