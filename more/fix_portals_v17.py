import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

ICONS_TO_IGNORE = {
    "rocket_launch", "query_stats", "nightlife", "person", "account_circle", 
    "notifications_active", "explore", "analytics", "support_agent", "settings_input_component",
    "calendar_today", "king_bed", "medical_services", "nutrition", "shield", "zoom_in", "zoom_out", "layers",
    "dashboard", "map", "tire_repair", "history", "warning", "arrow_right_alt", "check_circle", "monitoring",
    "menu", "close", "expand_more", "chevron_right", "power_settings_new", "sensors", "bolt", "thermostat", "local_gas_station"
}

def find_home_screen(screens, inner_folder):
    valid_screens = []
    for s in screens:
        if os.path.exists(os.path.join(inner_folder, s, "code.html")):
            valid_screens.append(s)
    if not valid_screens: return None
    priorities = ["home", "landing", "index", "welcome", "inicio", "start", "main", "portal", "dashboard", "overview", "hub", "race_control"]
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

    def find_match(text, current_href=None):
        raw_text = re.sub(r'<[^>]+>', ' ', text).replace("_", " ").strip()
        words = re.findall(r'\b\w+\b', raw_text.lower())
        filtered_words = [w for w in words if w not in ICONS_TO_IGNORE or len(words) == 1]
        clean_text = " ".join(filtered_words).strip()
        
        if not clean_text: 
            if words: clean_text = words[0]
            else: return None
        
        if any(w in clean_text for w in ["dashboard", "home", "logo", "back", "inicio", "overview", "race control", "main hub", "portal"]):
            return "index.html"

        search_phrases = [clean_text]
        if len(filtered_words) > 1: search_phrases.extend(filtered_words)

        # Tier 1: Direct Folder Name Match
        for phrase in search_phrases:
            for folder_norm, target in norm_map.items():
                if phrase == folder_norm or folder_norm.startswith(phrase):
                    if target != "index.html": return target

        # Tier 2: Substring Folder Name Match
        for phrase in search_phrases:
            if len(phrase) < 3: continue
            for folder_norm, target in norm_map.items():
                if phrase in folder_norm:
                    if target != "index.html": return target

        # Tier 3: Synonyms
        synonyms = {
            "locations": ["map", "track", "find", "address", "reach", "contact", "navigation", "destinations", "explorer"],
            "fleet": ["cars", "vehicles", "garage", "inventory", "models", "showroom", "deck", "voyager"],
            "booking": ["reserve", "appointment", "concierge", "book", "schedule", "checkout", "payment"],
            "concierge": ["booking", "service", "support", "help", "assistant"],
            "experience": ["360", "virtual", "tour", "explore", "cabin", "lounge", "view", "stellar"],
            "about": ["metadata", "info", "project", "story", "legacy", "details"],
            "mission": ["control", "status", "center", "destinations", "frontiers"],
            "stellar": ["lounge", "dining", "bar", "cabin", "experience"],
            "pit": ["wall", "strategy", "stops", "tire", "box"],
            "data": ["stream", "analytics", "telemetry", "stats", "graph", "stream"],
            "performance": ["driver", "stats", "profile", "telemetry", "apex"],
            "search": ["find", "lookup", "explore", "discover"]
        }
        
        for phrase in search_phrases:
            for key, syns in synonyms.items():
                if phrase == key or phrase in syns:
                    for folder_norm, target in norm_map.items():
                        if key in folder_norm or any(s in folder_norm for s in syns):
                            if target != "index.html": return target

        # Tier 4: Content Search
        for phrase in search_phrases:
            if len(phrase) < 4: continue
            for target, content in all_screens_content.items():
                if target == "index.html": continue
                lower_content = content.lower()
                if f"<title>{phrase}" in lower_content or f"h1>{phrase}" in lower_content: return target
                if len(phrase) >= 5 and phrase in lower_content: return target
        
        return None

    # Replace <a> tags
    a_pattern = re.compile(r'(<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)
    def replace_a(match):
        prefix, href, text, suffix = match.groups()
        if href.startswith(("http", "mailto", "tel", "javascript")): return match.group(0)
        
        match_target = find_match(text, href)
        if match_target:
            if href == "#" or href == "" or href == current_screen:
                return prefix.replace(f'href="{href}"', f'href="{match_target}"') + text + suffix
            if ".html" in href:
                current_norm = href.replace(".html", "").replace("_", " ").lower()
                text_clean = re.sub(r'<[^>]+>', ' ', text).replace("_", " ").lower()
                if not any(w in current_norm for w in text_clean.split()) and match_target != href:
                     return prefix.replace(f'href="{href}"', f'href="{match_target}"') + text + suffix
                     
        return match.group(0)
    html_content = a_pattern.sub(replace_a, html_content)

    # Fix buttons
    btn_pattern = re.compile(r'(<button\s+[^>]*>)(.*?)(</button>)', re.IGNORECASE | re.DOTALL)
    def replace_btn(match):
        tag_open, text, tag_close = match.groups()
        if 'onclick' in tag_open.lower(): return match.group(0)
        match_target = find_match(text)
        if match_target:
            new_tag = tag_open.replace("<button", f'<a href="{match_target}" style="display:inline-block; text-align:center; text-decoration:none; color:inherit;"').replace("button>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)
    html_content = btn_pattern.sub(replace_btn, html_content)

    # Interactive elements conversion
    inter_pattern = re.compile(r'(<(div|span|li|p|section)\s+[^>]*class=["\'][^"\']*(?:cursor-pointer|hover:|active:|group-hover:)[^"\']*["\'][^>]*>)(.*?)(</\2>)', re.IGNORECASE | re.DOTALL)
    def replace_inter(match):
        tag_open, tag_name, text, tag_close = match.groups()
        if "href=" in tag_open or "onclick=" in tag_open: return match.group(0)
        match_target = find_match(text)
        if match_target:
            display_style = "display:block;" if tag_name in ["div", "li", "p", "section"] else "display:inline-block;"
            new_tag = tag_open.replace(f"<{tag_name}", f'<a href="{match_target}" style="{display_style} text-decoration:none; color:inherit;"').replace(f"{tag_name}>", "a>")
            return f"{new_tag}{text}</a>"
        return match.group(0)
    html_content = inter_pattern.sub(replace_inter, html_content)

    # Navigator Logic
    nav_html = """
    <div id="stitch-nav" style="position:fixed; bottom:20px; left:20px; z-index:9999; font-family:sans-serif;">
        <button onclick="document.getElementById('stitch-nav-menu').style.display='block'; this.style.display='none'" style="background:rgba(0,0,0,0.8); color:white; border:1px solid rgba(255,255,255,0.2); padding:8px 12px; border-radius:20px; font-size:12px; cursor:pointer; backdrop-filter:blur(10px);">Explore Screens</button>
        <div id="stitch-nav-menu" style="display:none; background:rgba(0,0,0,0.9); color:white; border:1px solid rgba(255,255,255,0.2); padding:15px; border-radius:12px; min-width:200px; backdrop-filter:blur(20px); box-shadow:0 10px 30px rgba(0,0,0,0.5);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:5px;">
                <span style="font-size:10px; font-weight:bold; color:rgba(255,255,255,0.5); text-transform:uppercase;">Project Screens</span>
                <button onclick="document.getElementById('stitch-nav-menu').style.display='none'; document.querySelector('#stitch-nav > button').style.display='block'" style="background:none; border:none; color:white; cursor:pointer; font-size:16px;">&times;</button>
            </div>
            <ul style="list-style:none; padding:0; margin:0; max-height:300px; overflow-y:auto;">
    """
    for folder, target in sorted(screens_map.items()):
        name = folder.replace("_", " ").title()
        nav_html += f'<li style="margin:5px 0;"><a href="{target}" style="color:white; text-decoration:none; font-size:13px; opacity:0.7; transition:0.2s;" onmouseover="this.style.opacity=1" onmouseout="this.style.opacity=0.7">{name}</a></li>'
    nav_html += "</ul></div></div>"
    if "</body>" in html_content: html_content = html_content.replace("</body>", f"{nav_html}</body>")
    else: html_content += nav_html
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
        code_path = os.path.join(inner_folder, d, "code.html")
        if os.path.exists(code_path):
            target = "index.html" if d == home_screen else f"{d}.html"
            screens_map[d] = target
            with open(code_path, "r", encoding="utf-8") as f: all_screens_content[target] = f.read()
    for target_filename in screens_map.values():
        html = all_screens_content[target_filename]
        fixed_html = smart_link(html, screens_map, target_filename, all_screens_content)
        with open(os.path.join(project_path, target_filename), "w", encoding="utf-8") as f: f.write(fixed_html)
        if target_filename == "index.html":
            orig = [k for k, v in screens_map.items() if v == "index.html"][0]
            shutil.copy(os.path.join(project_path, "index.html"), os.path.join(project_path, f"{orig}.html"))
    print(f"Processed {folder_name} (Home: {home_screen})")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        try: process_project(f)
        except Exception as e: print(f"Error processing {f}: {e}")
