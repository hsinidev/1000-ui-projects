import os
import subprocess
import time
import sys

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"
START_PORT = 3004

def get_projects():
    return [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]

def run_servers():
    projects = get_projects()
    processes = []
    
    print(f"Found {len(projects)} projects.")
    
    for i, project in enumerate(projects):
        port = START_PORT + i
        project_path = os.path.join(BASE_DIR, project)
        
        # Using npx directly with Popen
        # We don't use 'start /B' here because Popen already starts it in the background
        # We keep the process objects in a list to prevent them from being GC'd immediately
        cmd = ["npx", "http-server", project_path, "-p", str(port), "--cors", "-c-1"]
        try:
            # On Windows, we need to handle the shell for npx if it's a .cmd
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            processes.append(p)
            print(f"[{i+1}/{len(projects)}] Started {project} on http://127.0.0.1:{port}")
        except Exception as e:
            print(f"Failed to start {project}: {e}")
    
    print("\nAll servers started. Keeping script alive...")
    try:
        # Keep the script alive for a very long time (e.g., 24 hours)
        # This ensures the child processes stay alive if they are tied to this process
        time.sleep(86400) 
    except KeyboardInterrupt:
        print("Shutting down...")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    run_servers()
