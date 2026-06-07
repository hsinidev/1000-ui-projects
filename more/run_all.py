import os
import subprocess
import time

BASE_DIR = r"c:\Users\hsini\Desktop\34project\more"
START_PORT = 3004

def get_projects():
    return [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("stitch_")]

def run_servers():
    projects = get_projects()
    links = []
    
    print(f"Found {len(projects)} projects.")
    
    for i, project in enumerate(projects):
        port = START_PORT + i
        project_path = os.path.join(BASE_DIR, project)
        
        # Command to run http-server in the background
        # Using start /B on windows to run in background
        cmd = f'start /B npx http-server "{project_path}" -p {port} --cors'
        subprocess.Popen(cmd, shell=True)
        
        url = f"http://127.0.0.1:{port}"
        links.append(f"- [{project.replace('_', ' ').title()}]({url})")
        print(f"Starting {project} on {url}...")
    
    print("\n### Project Links\n")
    print("\n".join(links))

if __name__ == "__main__":
    run_servers()
