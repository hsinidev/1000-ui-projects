import os
import re
import shutil

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"

ICONS_TO_IGNORE = {
    "rocket_launch", "query_stats", "nightlife", "person", "account_circle", 
    "notifications_active", "explore", "analytics", "support_agent", "settings_input_component",
    "calendar_today", "king_bed", "medical_services", "nutrition", "shield", "zoom_in", "zoom_out", "layers",
    "dashboard", "map", "tire_repair", "history", "warning", "arrow_right_alt", "check_circle", "monitoring",
    "menu", "close", "expand_more", "chevron_right", "power_settings_new", "sensors", "bolt", "thermostat", "local_gas_station",
    "notifications", "settings", "person", "emergency", "hub", "dashboard", "terminal", "help_center", "search", "mail", "public",
    "verified_user", "safety_check", "electric_bolt", "shield_with_heart", "star", "lan", "memory", "database", "security", "account_tree"
}

def find_home_screen(screens, inner_folder):
    valid_screens = []
    for s in screens:
        if os.path.exists(os.path.join(inner_folder, s, "code.html")):
            valid_screens.append(s)
    if not valid_screens: return None
    priorities = ["home", "landing", "index", "welcome", "inicio", "start", "main", "portal", "dashboard", "overview", "hub", "race_control", "operations", "discovery", "explorer"]
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower().split('_'): return screen
    for p in priorities:
        for screen in valid_screens:
            if p in screen.lower(): return screen
    return valid_screens[0]

def find_match(text, norm_map, current_screen, exclude_current=True):
    raw_text = re.sub(r'<[^>]+>', ' ', text).replace("_", " ").strip()
    words = re.findall(r'\b\w+\b', raw_text.lower())
    filtered_words = [w for w in words if w not in ICONS_TO_IGNORE or len(words) <= 1]
    clean_text = " ".join(filtered_words).strip()
    if not clean_text: 
        if words: clean_text = words[0]
        else: return None
    search_phrases = [clean_text]
    if len(filtered_words) > 1: search_phrases.extend(filtered_words)
    for phrase in search_phrases:
        for folder_norm, target in norm_map.items():
            if exclude_current and target == current_screen: continue
            if phrase == folder_norm: return target
            if folder_norm.startswith(phrase) or phrase.startswith(folder_norm): return target
            if len(phrase) > 3 and phrase in folder_norm: return target
    synonyms = {
        "locations": ["map", "track", "find", "address", "reach", "contact", "navigation", "destinations", "explorer", "network", "topology", "services", "area"],
        "fleet": ["cars", "vehicles", "garage", "inventory", "models", "showroom", "deck", "voyager", "collection"],
        "booking": ["reserve", "appointment", "concierge", "book", "schedule", "checkout", "payment", "reservation", "inquiry", "request"],
        "concierge": ["booking", "service", "support", "help", "assistant", "contact"],
        "experience": ["360", "virtual", "tour", "explore", "cabin", "lounge", "view", "stellar", "gallery", "portfolio", "discovery"],
        "about": ["metadata", "info", "project", "story", "legacy", "details", "company", "team", "mission", "vision"],
        "mission": ["control", "status", "center", "destinations", "frontiers", "command", "ops"],
        "stellar": ["lounge", "dining", "bar", "cabin", "experience"],
        "pit": ["wall", "strategy", "stops", "tire", "box"],
        "data": ["stream", "analytics", "telemetry", "stats", "graph", "stream", "logs", "metrics"],
        "performance": ["driver", "stats", "profile", "telemetry", "apex"],
        "search": ["find", "lookup", "explore", "discover", "query"],
        "resources": ["assets", "management", "inventory", "tools", "seasonal", "techniques", "books", "journal", "newsletter", "ethics"],
        "network": ["topology", "infrastructure", "connectivity", "nodes", "compute", "storage", "infra", "security", "threats"],
        "support": ["help", "contact", "faq", "customer", "service"],
        "profile": ["account", "user", "settings", "login", "signup", "dashboard"]
    }
    for phrase in search_phrases:
        for key, syns in synonyms.items():
            if phrase == key or phrase in syns:
                for folder_norm, target in norm_map.items():
                    if exclude_current and target == current_screen: continue
                    if key in folder_norm or any(s in folder_norm for s in syns):
                        return target
    home_triggers = ["dashboard", "home", "logo", "back", "inicio", "overview", "race control", "main hub", "portal", "operations", "city control", "system active", "discover", "neural_core", "terminal_core", "orbital luxe"]
    if any(w in clean_text for w in home_triggers):
        return "index.html"
    return None

def smart_link(html_content, screens_map, current_screen):
    norm_map = {}
    for folder, target in screens_map.items():
        norm_map[folder.lower().replace("_", " ")] = target
    
    html_content = re.sub(r'<class=', '<a class=', html_content)

    # Simplified unified pattern to avoid group errors
    a_pattern = re.compile(r'(?is)<a\s+([^>]*?)>(.*?)</a>')
    def a_callback(match):
        attrs, inner = match.group(1), match.group(2)
        href_match = re.search(r'href=["\']([^"\']*)["\']', attrs, re.I)
        href = href_match.group(1) if href_match else ""
        if href.startswith(("http", "mailto", "tel", "javascript")): return match.group(0)
        text = re.sub(r'<[^>]+>', ' ', inner).strip()
        match_target = find_match(text, norm_map, current_screen, exclude_current=(href == current_screen))
        if not match_target and href in ["#", "", current_screen]: match_target = "index.html"
        if match_target and match_target != href:
            if href_match:
                new_attrs = re.sub(r'href=["\'][^"\']*["\']', f'href="{match_target}"', attrs, flags=re.I)
            else:
                new_attrs = attrs + f' href="{match_target}"'
            return f'<a {new_attrs}>{inner}</a>'
        return match.group(0)

    btn_pattern = re.compile(r'(?is)<button\s+([^>]*?)>(.*?)</button>')
    def btn_callback(match):
        attrs, inner = match.group(1), match.group(2)
        if 'onclick' in attrs.lower(): return match.group(0)
        text = re.sub(r'<[^>]+>', ' ', inner).strip()
        match_target = find_match(text, norm_map, current_screen) or "index.html"
        return f'<a href="{match_target}" style="display:inline-block; text-align:center; text-decoration:none; color:inherit;" {attrs}>{inner}</a>'

    inter_pattern = re.compile(r'(?is)<(div|span|li|p|section)\s+([^>]*?class=["\'][^"\']*(?:cursor-pointer|hover:|active:|group-hover:)[^"\']*["\'][^>]*?)>(.*?)</\1>')
    def inter_callback(match):
        tag, attrs, inner = match.group(1), match.group(2), match.group(3)
        if "<a " in inner.lower(): return match.group(0)
        text = re.sub(r'<[^>]+>', ' ', inner).strip()
        match_target = find_match(text, norm_map, current_screen) or "index.html"
        display = "display:block;" if tag in ["div", "li", "p", "section"] else "display:inline-block;"
        return f'<a href="{match_target}" style="{display} text-decoration:none; color:inherit;" {attrs}>{inner}</a>'

    html_content = a_pattern.sub(a_callback, html_content)
    html_content = btn_pattern.sub(btn_callback, html_content)
    html_content = inter_pattern.sub(inter_callback, html_content)

    # Aggressive dead link fixing in common areas
    def fix_dead_links(m):
        return re.sub(r'href=["\']#["\']', 'href="index.html"', m.group(0))
    
    for tag in ["header", "footer", "nav", "aside"]:
        html_content = re.sub(r'(?is)<' + tag + r'[^>]*>.*?</' + tag + r'>', fix_dead_links, html_content)

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
    
    html_content = re.sub(r'<div id="stitch-nav".*?</div>\s*</div>', '', html_content, flags=re.DOTALL)
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
        fixed_html = smart_link(html, screens_map, target_filename)
        with open(os.path.join(project_path, target_filename), "w", encoding="utf-8") as f: f.write(fixed_html)
        if target_filename == "index.html":
            orig = [k for k, v in screens_map.items() if v == "index.html"][0]
            shutil.copy(os.path.join(project_path, "index.html"), os.path.join(project_path, f"{orig}.html"))
    print(f"Processed {folder_name}")

if __name__ == "__main__":
    folders = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]
    for f in folders:
        try: process_project(f)
        except Exception as e: print(f"Error processing {f}: {e}")
