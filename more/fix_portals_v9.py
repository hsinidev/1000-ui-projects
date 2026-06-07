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
    
    priorities = ["home", "landing", "index", "welcome", "inicio", "start", "main", "portal", "dashboard", "overview", "hub"]
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower().split('_'): return screen
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower(): return screen
    return valid_screens[0]

def smart_link(html_content, screens_map, current_screen, all_screens_content):
    # screens_map: { "folder_name": "target_filename.html" }
    # all_screens_content: { "target_filename.html": "full html content" }
    
    norm_map = {}
    for folder, target in screens_map.items():
        norm_map[folder.lower().replace("_", " ")] = target

    def find_match(text):
        text = text.lower().strip()
        if not text: return None
        
        # 1. Exact match with a folder name
        for folder_norm, target in norm_map.items():
            if text == folder_norm or (len(text) > 3 and text in folder_norm):
                if target != "index.html" or len(norm_map) == 1:
                    return target
        
        # 2. Specialized synonyms
        synonyms = {
            "locations": ["map", "pickup", "find", "address", "reach", "contact", "navigation"],
            "fleet": ["cars", "vehicles", "garage", "inventory", "models", "showroom", "deck"],
            "booking": ["reserve", "appointment", "concierge", "book", "schedule", "checkout", "payment"],
            "concierge": ["booking", "service", "support", "help", "assistant", "chat"],
            "experience": ["360", "virtual", "tour", "explore", "cabin", "lounge"],
            "home": ["index", "main", "inicio", "start", "welcome", "logo", "portal"],
            "about": ["metadata", "info", "project", "story", "legacy", "details"],
            "mission control": ["destinations", "explorer", "frontiers", "navigation", "status"],
            "stellar lounge": ["cabin", "experience", "luxury", "bar", "dining"]
        }
        
        for key, syns in synonyms.items():
            if text == key or any(s == text for s in syns):
                for folder_norm, target in norm_map.items():
                    if key in folder_norm or any(s in folder_norm for s in syns):
                        if target != "index.html" or len(norm_map) == 1:
                            return target
        
        # 3. CONTENT-AWARE MATCHING (NEW)
        # Search for the link text in the content of other screens
        # If the text exists in another screen (especially in a title or header), link to it.
        potential_targets = []
        for target, content in all_screens_content.items():
            if target == "index.html" and current_screen == "index.html": continue
            # Check for the text in a semi-prominent way (e.g. not just in a hidden script)
            # We look for text in headers or spans
            if text in content.lower():
                # Score it: if it's in a <title> or <h1>, it's a very strong match
                if f"<title>{text}" in content.lower() or f"<h1>{text}" in content.lower() or f"<h2>{text}" in content.lower():
                    return target
                potential_targets.append(target)
        
        if potential_targets:
            # Pick the most likely one (first non-index if possible)
            for t in potential_targets:
                if t != "index.html": return t
            return potential_targets[0]

        # 4. Fallback
        if any(w in text for w in ["home", "logo", "back", "inicio"]):
            return "index.html"
            
        return None

    # Fix <a> tags
    a_pattern = re.compile(r'(<a\s+[^>]*href=["\']#["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    def replace_a(match):
        prefix, text, suffix = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        match_target = find_match(clean_text)
        if match_target:
            return prefix.replace('href="#"', f'href="{match_target}"') + text + suffix
        return match.group(0)
    
    html_content = a_pattern.sub(replace_a, html_content)

    # Fix <button> tags
    btn_pattern = re.compile(r'(<button\s+[^>]*>)(.*?)(</button>)', re.IGNORECASE | re.DOTALL)
    def replace_btn(match):
        tag_open, text, tag_close = match.groups()
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        match_target = find_match(clean_text)
        if match_target:
            new_tag = tag_open.replace("<button", f'<a href="{match_target}" style="display:inline-block; text-align:center;"').replace("button>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)

    html_content = btn_pattern.sub(replace_btn, html_content)

    # ... Navigator Logic ...
    nav_html = """
    <!-- Project Screen Navigator -->
    <div id="stitch-nav" style="position:fixed; bottom:20px; left:20px; z-index:9999; font-family:sans-serif;">
        <button onclick="document.getElementById('stitch-nav-menu').style.display='block'; this.style.display='none'" style="background:rgba(0,0,0,0.8); color:white; border:1px solid rgba(255,255,255,0.2); padding:8px 12px; border-radius:20px; font-size:12px; cursor:pointer; backdrop-filter:blur(10px);">Explore Screens</button>
        <div id="stitch-nav-menu" style="display:none; background:rgba(0,0,0,0.9); color:white; border:1px solid rgba(255,255,255,0.2); padding:15px; border-radius:12px; min-width:200px; backdrop-filter:blur(20px); box-shadow:0 10px 30px rgba(0,0,0,0.5);">
            <div style="display:flex; justify-between:items-center; margin-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:5px;">
                <span style="font-size:10px; font-weight:bold; color:rgba(255,255,255,0.5); text-transform:uppercase;">Project Screens</span>
                <button onclick="document.getElementById('stitch-nav-menu').style.display='none'; document.querySelector('#stitch-nav > button').style.display='block'" style="background:none; border:none; color:white; cursor:pointer; font-size:16px;">&times;</button>
            </div>
            <ul style="list-style:none; padding:0; margin:0; max-height:300px; overflow-y:auto;">
    """
    for folder, target in screens_map.items():
        name = folder.replace("_", " ").title()
        nav_html += f'<li style="margin:5px 0;"><a href="{target}" style="color:white; text-decoration:none; font-size:13px; opacity:0.7; transition:0.2s;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.7">{name}</a></li>'
    nav_html += "</ul></div></div>"
    
    if "</body>" in html_content:
        html_content = html_content.replace("</body>", f"{nav_html}</body>")
    else:
        html_content += nav_html

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
    all_screens_content = {}
    for d in screen_dirs:
        if os.path.exists(os.path.join(inner_folder, d, "code.html")):
            target = "index.html" if d == home_screen else f"{d}.html"
            screens_map[d] = target
            with open(os.path.join(inner_folder, d, "code.html"), "r", encoding="utf-8") as f:
                all_screens_content[target] = f.read()

    for d, target_filename in screens_map.items():
        code_path = os.path.join(inner_folder, d, "code.html")
        html = all_screens_content[target_filename]
        fixed_html = smart_link(html, screens_map, target_filename, all_screens_content)
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
