import os
import re

DEV_INFO = {
    "name": "HSINI MOHAMED",
    "website": "hsini.dev",
    "email": "contact@hsini.dev",
    "phone": "+212658029773",
    "photo": "232697467.jpg",
    "github": "https://github.com/hsinidev",
    "linkedin": "https://www.linkedin.com/in/hsinidev/"
}

footer_branding = f"""
    <div class="personal-footer" style="margin: 80px auto 40px; padding: 40px 20px; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; font-family: sans-serif; background: rgba(0,0,0,0.3); width: 100%; max-width: 1200px; border-radius: 24px; backdrop-filter: blur(10px); position: relative; z-index: 1000;">
        <img src="{DEV_INFO['photo']}" alt="{DEV_INFO['name']}" style="width: 80px; height: 80px; border-radius: 50%; border: 3px solid #ff6b00; margin: 0 auto 20px; box-shadow: 0 0 30px rgba(255,107,0,0.2);">
        <p style="color: #fff; font-size: 20px; margin-bottom: 8px; font-weight: 700; letter-spacing: 1px;">{DEV_INFO['name']}</p>
        <p style="color: rgba(255,255,255,0.5); font-size: 14px; margin-bottom: 24px; font-weight: 400;">Full-Stack Engineer & Digital Architect</p>
        
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">
            <a href="{DEV_INFO['github']}" target="_blank" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s; border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; gap: 8px;">
                GitHub
            </a>
            <a href="{DEV_INFO['linkedin']}" target="_blank" style="color: #fff; text-decoration: none; background: #0077b5; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s; display: flex; align-items: center; gap: 8px;">
                LinkedIn
            </a>
        </div>

        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 30px; font-size: 13px; color: rgba(255,255,255,0.7);">
            <a href="https://{DEV_INFO['website']}" style="color: #ff6b00; text-decoration: none; font-weight: 600; border-bottom: 1px solid rgba(255,107,0,0.3); padding-bottom: 2px;">{DEV_INFO['website']}</a>
            <a href="mailto:{DEV_INFO['email']}" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2px;">{DEV_INFO['email']}</a>
            <a href="tel:{DEV_INFO['phone']}" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2px;">{DEV_INFO['phone']}</a>
        </div>
        <p style="margin-top: 40px; color: rgba(255,255,255,0.15); font-size: 11px; letter-spacing: 2px; text-transform: uppercase;">© 2024 HSINI.DEV | All Rights Reserved</p>
    </div>
"""

path = r"c:\Users\hsini\Desktop\34project\more\stitch_zenith_orbital_interface\index.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Clean up
html = re.sub(r'<div class="personal-footer".*?</div>', '', html, flags=re.DOTALL)
html = re.sub(r'</body>', f'{footer_branding}\n</body>', html, flags=re.IGNORECASE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done testing on Zenith")
