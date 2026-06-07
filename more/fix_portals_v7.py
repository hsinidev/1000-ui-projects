import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

def find_home_screen(screens, inner_folder):
    valid_screens = []
    for s in screens:
        if os.path.exists(os.path.join(inner_folder, s, "code.html")):
            valid_screens.append(s)
    if not valid_screens: return None
    priorities = ["home", "dashboard", "index", "main", "portal", "landing", "overview", "selector", "inicio", "start", "welcome", "hub"]
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower(): return screen
    return valid_screens[0]

def smart_link(html_content, screens_map):
    # screens_map: { "folder_name": "target_filename.html" }
    
    # 1. Normalize folder names for matching
    norm_map = {}
    for folder, target in screens_map.items():
        norm_map[folder.lower().replace("_", " ")] = target

    # 2. Function to find best match for a text string
    def find_match(text):
        text = text.lower().strip()
        if not text: return None
        
        # Exact or close match
        for folder_norm, target in norm_map.items():
            if text in folder_norm or folder_norm in text:
                return target
        
        # Specialized synonyms
        synonyms = {
            "locations": ["map", "pickup", "find", "reach"],
            "fleet": ["cars", "vehicles", "garage", "inventory"],
            "booking": ["reserve", "appointment", "concierge"],
            "concierge": ["booking", "service", "support"],
            "experience": ["360", "virtual", "tour"],
            "home": ["index", "main", "inicio"],
            "about": ["metadata", "info", "project"]
        }
        
        for key, syns in synonyms.items():
            if text == key or any(s in text for s in syns):
                # Look for a folder that matches any of these syns
                for folder_norm, target in norm_map.items():
                    if key in folder_norm or any(s in folder_norm for s in syns):
                        return target
        return None

    # 3. Fix <a> tags
    a_pattern = re.compile(r'(<a\s+[^>]*href=["\']#["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    def replace_a(match):
        prefix, text, suffix = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        match_target = find_match(clean_text)
        if match_target:
            return prefix.replace('href="#"', f'href="{match_target}"') + text + suffix
        # Fallback to index if it looks like a logo or home link
        if any(w in clean_text.lower() for w in ["home", "logo", "back"]):
            return prefix.replace('href="#"', 'href="index.html"') + text + suffix
        return match.group(0)
    
    html_content = a_pattern.sub(replace_a, html_content)

    # 4. Fix <button> tags by converting them to <a> or adding onclick
    # We'll try to convert them to <a> to be safe for static deployment
    btn_pattern = re.compile(r'(<button\s+[^>]*>)(.*?)(</button>)', re.IGNORECASE | re.DOTALL)
    def replace_btn(match):
        tag_open, text, tag_close = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        match_target = find_match(clean_text)
        if match_target:
            # Convert <button ...> to <a href="..." ... style="display:inline-block">
            # We preserve classes but change tag
            new_tag = tag_open.replace("<button", f'<a href="{match_target}" style="display:inline-block; text-align:center;"').replace("button>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)

    html_content = btn_pattern.sub(replace_btn, html_content)

    # 5. Fix common file patterns
    for folder, target in screens_map.items():
        html_content = html_content.replace(f'href="{folder}.html"', f'href="{target}"')
        html_content = html_content.replace(f'href="./{folder}.html"', f'href="{target}"')

    return html_content

def process_project(folder_name):
    project_path = os.path.join(BASE_DIR, folder_name)
    inner_folder = os.path.join(project_path, folder_name)
    if not os.path.exists(inner_folder): inner_folder = project_path
    
    screen_dirs = [d for d in os.listdir(inner_folder) if os.path.isdir(os.path.join(inner_folder, d)) and d != folder_name]
    home_screen = find_home_screen(screen_dirs, inner_folder)
    if not home_screen: return

    screens_map = {}
    for d in screen_dirs:
        if os.path.exists(os.path.join(inner_folder, d, "code.html")):
            screens_map[d] = "index.html" if d == home_screen else f"{d}.html"

    for d, target_filename in screens_map.items():
        code_path = os.path.join(inner_folder, d, "code.html")
        with open(code_path, "r", encoding="utf-8") as f:
            html = f.read()
        
        fixed_html = smart_link(html, screens_map)
        target_path = os.path.join(project_path, target_filename)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(fixed_html)
        
        if d == home_screen:
            shutil.copy(target_path, os.path.join(project_path, f"{d}.html"))

    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        try: process_project(f)
        except Exception as e: print(f"Error processing {f}: {e}")
