import os
import subprocess
import time
import sys

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"
START_PORT = 3004

def get_projects():
    return sorted([d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")])

def kill_existing():
    print("Attempting to clear existing node processes on target ports...")
    try:
        # Kill any node processes to be sure ports are free
        subprocess.run(["taskkill", "/F", "/IM", "node.exe", "/T"], capture_output=True)
    except:
        pass

def run_servers():
    projects = get_projects()
    links = []
    
    # We'll use npx http-server to be safer
    for i, project in enumerate(projects):
        port = START_PORT + i
        project_path = os.path.join(BASE_DIR, project)
        
        # Start server in background
        cmd = f'npx http-server "{project_path}" -p {port} --cors -c-1'
        subprocess.Popen(cmd, shell=True, cwd=BASE_DIR)
        
        url = f"http://127.0.0.1:{port}"
        links.append(f"| {project} | [{url}]({url}) |")
        print(f"Started {project} on {url}")
        time.sleep(0.5)

    # Save links to a markdown file
    with open(os.path.join(BASE_DIR, "project_links.md"), "w") as f:
        f.write("# Project Portal Links\n\n")
        f.write("| Project Name | Local Link |\n")
        f.write("| :--- | :--- |\n")
        f.write("\n".join(links))

if __name__ == "__main__":
    kill_existing()
    run_servers()
