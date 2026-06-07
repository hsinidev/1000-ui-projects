import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

ICONS_TO_IGNORE = {
    "rocket_launch", "query_stats", "nightlife", "person", "account_circle", 
    "notifications_active", "explore", "analytics", "support_agent", "settings_input_component",
    "calendar_today", "king_bed", "medical_services", "nutrition", "shield", "zoom_in", "zoom_out", "layers",
    "dashboard", "map", "tire_repair", "history", "warning", "arrow_right_alt"
}

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
    norm_map = {}
    for folder, target in screens_map.items():
        norm_map[folder.lower().replace("_", " ")] = target

    def find_match(text):
        raw_text = re.sub(r'<[^>]+>', ' ', text).lower()
        words = raw_text.split()
        filtered_words = [w for w in words if w not in ICONS_TO_IGNORE and len(w) > 2]
        clean_text = " ".join(filtered_words).strip()
        if not clean_text: return None
        
        search_phrases = [clean_text]
        if len(filtered_words) > 1: search_phrases.extend(filtered_words)

        for phrase in search_phrases:
            for folder_norm, target in norm_map.items():
                if phrase == folder_norm or (len(phrase) > 3 and phrase in folder_norm):
                    if target != "index.html" or len(norm_map) == 1: return target
            
            synonyms = {
                "locations": ["map", "pickup", "find", "address", "reach", "contact", "navigation", "destinations", "track"],
                "fleet": ["cars", "vehicles", "garage", "inventory", "models", "showroom", "deck"],
                "booking": ["reserve", "appointment", "concierge", "book", "schedule", "checkout", "payment"],
                "concierge": ["booking", "service", "support", "help", "assistant", "chat"],
                "experience": ["360", "virtual", "tour", "explore", "cabin", "lounge"],
                "home": ["index", "main", "inicio", "start", "welcome", "logo", "portal", "dashboard"],
                "about": ["metadata", "info", "project", "story", "legacy", "details"],
                "mission control": ["destinations", "explorer", "frontiers", "navigation", "status", "control"],
                "stellar lounge": ["cabin", "experience", "luxury", "bar", "dining", "lounge"],
                "pit wall": ["strategy", "race", "timing", "wall", "stops"],
                "data stream": ["analytics", "telemetry", "stats", "graph"]
            }
            
            for key, syns in synonyms.items():
                if phrase == key or any(s == phrase for s in syns):
                    for folder_norm, target in norm_map.items():
                        if key in folder_norm or any(s in folder_norm for s in syns):
                            if target != "index.html" or len(norm_map) == 1: return target
            
            for target, content in all_screens_content.items():
                if target == "index.html" and current_screen == "index.html": continue
                if phrase in content.lower():
                    if f"<title>{phrase}" in content.lower() or f"<h1>{phrase}" in content.lower(): return target
                    return target
        if any(w in clean_text for w in ["home", "logo", "back", "inicio"]): return "index.html"
        return None

    # Fix <a> tags
    a_pattern = re.compile(r'(<a\s+[^>]*href=["\']#["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    def replace_a(match):
        prefix, text, suffix = match.groups()
        match_target = find_match(text)
        if match_target: return prefix.replace('href="#"', f'href="{match_target}"') + text + suffix
        return match.group(0)
    html_content = a_pattern.sub(replace_a, html_content)

    # Fix <button> tags
    btn_pattern = re.compile(r'(<button\s+[^>]*>)(.*?)(</button>)', re.IGNORECASE | re.DOTALL)
    def replace_btn(match):
        tag_open, text, tag_close = match.groups()
        match_target = find_match(text)
        if match_target:
            new_tag = tag_open.replace("<button", f'<a href="{match_target}" style="display:inline-block; text-align:center;"').replace("button>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)
    html_content = btn_pattern.sub(replace_btn, html_content)

    # NEW: Fix <div> tags that act as links (contain cursor-pointer)
    div_pattern = re.compile(r'(<div\s+[^>]*class=["\'][^"\']*cursor-pointer[^"\']*["\'][^>]*>)(.*?)(</div>)', re.IGNORECASE | re.DOTALL)
    def replace_div(match):
        tag_open, text, tag_close = match.groups()
        # Only convert if it contains text that matches a screen
        match_target = find_match(text)
        if match_target:
            # Check if it already has an onclick or is likely a link
            new_tag = tag_open.replace("<div", f'<a href="{match_target}" style="display:block; text-decoration:none;"').replace("div>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)
    html_content = div_pattern.sub(replace_div, html_content)

    # Navigator Logic
    nav_html = """
    <!-- Project Screen Navigator -->
    <div id="stitch-nav" style="position:fixed; bottom:20px; left:20px; z-index:9999; font-family:sans-serif;">
        <button onclick="document.getElementById('stitch-nav-menu').style.display='block'; this.style.display='none'" style="background:rgba(0,0,0,0.8); color:white; border:1px solid rgba(255,255,255,0.2); padding:8px 12px; border-radius:20px; font-size:12px; cursor:pointer; backdrop-filter:blur(10px);">Explore Screens</button>
        <div id="stitch-nav-menu" style="display:none; background:rgba(0,0,0,0.9); color:white; border:1px solid rgba(255,255,255,0.2); padding:15px; border-radius:12px; min-width:200px; backdrop-filter:blur(20px); box-shadow:0 10px 30px rgba(0,0,0,0.5);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:5px;">
                <span style="font-size:10px; font-weight:bold; color:rgba(255,255,255,0.5); text-transform:uppercase;">Project Screens</span>
                <button onclick="document.getElementById('stitch-nav-menu').style.display='none'; document.querySelector('#stitch-nav > button').style.display='block'" style="background:none; border:none; color:white; cursor:pointer; font-size:16px;">&times;</button>
            </div>
            <ul style="list-style:none; padding:0; margin:0; max-height:300px; overflow-y:auto;">
    """
    for folder, target in screens_map.items():
        name = folder.replace("_", " ").title()
        nav_html += f'<li style="margin:5px 0;"><a href="{target}" style="color:white; text-decoration:none; font-size:13px; opacity:0.7; transition:0.2s;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.7">{name}</a></li>'
    nav_html += "</ul></div></div>"
    if "</body>" in html_content: html_content = html_content.replace("</body>", f"{nav_html}</body>")
    else: html_content += nav_html

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
            with open(os.path.join(inner_folder, d, "code.html"), "r", encoding="utf-8") as f: all_screens_content[target] = f.read()
    for d, target_filename in screens_map.items():
        html = all_screens_content[target_filename]
        fixed_html = smart_link(html, screens_map, target_filename, all_screens_content)
        target_path = os.path.join(project_path, target_filename)
        with open(target_path, "w", encoding="utf-8") as f: f.write(fixed_html)
        if d == home_screen: shutil.copy(target_path, os.path.join(project_path, f"{d}.html"))
    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        try: process_project(f)
        except Exception as e: print(f"Error processing {f}: {e}")
