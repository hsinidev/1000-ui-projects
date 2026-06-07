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
    
    print(f"Found {len(projects)} projects.", flush=True)
    
    for i, project in enumerate(projects):
        port = START_PORT + i
        project_path = os.path.join(BASE_DIR, project)
        
        # Using npx -y to skip confirmation
        cmd = ["npx", "-y", "http-server", project_path, "-p", str(port), "--cors", "-c-1"]
        try:
            p = subprocess.Popen(cmd, shell=True)
            processes.append(p)
            print(f"[{i+1}/{len(projects)}] Started {project} on http://127.0.0.1:{port}", flush=True)
        except Exception as e:
            print(f"Failed to start {project}: {e}", flush=True)
        
        # Add a small delay to avoid overwhelming the system/npx
        time.sleep(0.5)
    
    print("\nAll servers started. Keeping script alive...", flush=True)
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Shutting down...", flush=True)
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    run_servers()
