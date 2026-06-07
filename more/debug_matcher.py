import os
import re

ICONS_TO_IGNORE = {"dashboard", "map", "tire_repair", "history", "query_stats"} # Simplified for test

def find_match(text, norm_map, all_screens_content, current_screen="index.html"):
    raw_text = re.sub(r'<[^>]+>', ' ', text).strip()
    words = re.findall(r'\b\w+\b', raw_text.lower())
    filtered_words = [w for w in words if w not in ICONS_TO_IGNORE or len(words) == 1]
    clean_text = " ".join(filtered_words).strip()
    
    print(f"DEBUG: Processing '{text}' -> clean: '{clean_text}'")
    
    if any(w in clean_text for w in ["dashboard", "home"]): return "index.html"

    search_phrases = [clean_text]
    if len(filtered_words) > 1: search_phrases.extend(filtered_words)

    # Tier 1 & 2
    for phrase in search_phrases:
        for folder_norm, target in norm_map.items():
            if phrase == folder_norm or (len(phrase) >= 3 and phrase in folder_norm):
                print(f"DEBUG: Match Tier 1/2: '{phrase}' matched folder '{folder_norm}' -> {target}")
                return target
    
    # Tier 3: Synonyms
    synonyms = {
        "pit": ["wall", "strategy", "stops", "tire"],
        "data": ["stream", "analytics", "telemetry", "stats"],
    }
    for phrase in search_phrases:
        for key, syns in synonyms.items():
            if phrase == key or phrase in syns:
                for folder_norm, target in norm_map.items():
                    if key in folder_norm or any(s in folder_norm for s in syns):
                        print(f"DEBUG: Match Tier 3: '{phrase}' matched synonym for '{folder_norm}' -> {target}")
                        return target

    # Tier 4/5: Content
    for phrase in search_phrases:
        if len(phrase) < 4: continue
        for target, content in all_screens_content.items():
            if phrase in content.lower():
                print(f"DEBUG: Match Tier 4/5: '{phrase}' matched content in {target}")
                return target
    return None

norm_map = {
    'driver performance profile': 'driver_performance_profile.html',
    'pit wall strategy': 'pit_wall_strategy.html',
    'race control dashboard': 'index.html',
    'telemetry analytics': 'telemetry_analytics.html'
}

# Dummy contents
all_contents = {
    'driver_performance_profile.html': 'This is a driver performance profile.',
    'pit_wall_strategy.html': 'This is the pit wall strategy strategy.',
    'index.html': 'Race Control Dashboard home.',
    'telemetry_analytics.html': 'Telemetry analytics data stream.'
}

print("--- Testing PIT_STOPS ---")
find_match("PIT_STOPS", norm_map, all_contents)

print("\n--- Testing DATA_STREAM ---")
find_match("DATA_STREAM", norm_map, all_contents)

print("\n--- Testing TRACK_MAP ---")
find_match("TRACK_MAP", norm_map, all_contents)
