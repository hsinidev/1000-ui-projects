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

def inject_seo(html_path, project_name):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. TOTAL RESET OF FOOTER AREA
        # We find the end of the original footer (</footer>) and keep everything before it.
        # Then we keep the </body> tag.
        # Everything in between is cleared of our branding to avoid duplication.
        
        if '</footer>' in html:
            parts = html.split('</footer>', 1)
            main_content = parts[0] + '</footer>'
            rest = parts[1]
            
            # Clean 'rest' from any of our previous injections
            rest = re.sub(r'<div class="personal-footer".*?</div>', '', rest, flags=re.DOTALL)
            rest = re.sub(r'<div id="stitch-nav".*?</div>\s*</div>', '', rest, flags=re.DOTALL)
            # Remove any lingering copyright or link fragments
            rest = re.sub(r'<p style="margin-top: 40px;.*?© 2024 HSINI\.DEV.*?</p>', '', rest, flags=re.DOTALL)
            rest = re.sub(r'<div style="display: flex; justify-content: center;.*?hsini\.dev.*?</div>', '', rest, flags=re.DOTALL)
            # Remove extra closing divs that might have leaked
            rest = re.sub(r'</div>\s*</div>\s*</div>', '', rest) # Very specific cleanup for seen leakage
            
            # Reconstruct HTML base
            html = main_content + rest

        # 2. SEO META CLEANUP
        html = re.sub(r'<!-- JSON-LD Schema -->.*?({.*?})?.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
        html = re.sub(r'<meta name="description" content=".*?">', '', html)
        html = re.sub(r'<meta name="keywords" content=".*?">', '', html)
        html = re.sub(r'<meta name="author" content=".*?">', '', html)
        html = re.sub(r'<!-- Open Graph / Facebook -->.*?<!-- Twitter -->', '', html, flags=re.DOTALL)
        html = re.sub(r'<!-- Twitter -->.*?<!-- GEO Tags -->', '', html, flags=re.DOTALL)
        html = re.sub(r'<!-- GEO Tags -->.*?<!-- JSON-LD Schema -->', '', html, flags=re.DOTALL)

        # 3. PREPARE NEW SEO BLOCK
        clean_name = project_name.replace('stitch_', '').replace('_', ' ').title()
        is_index = os.path.basename(html_path) == 'index.html'
        page_title = f"{clean_name} | Full-Stack Developer - {DEV_INFO['name']}"
        if not is_index:
            page_title = f"{clean_name} - {os.path.basename(html_path).replace('.html', '').replace('_', ' ').title()} | {DEV_INFO['name']}"

        seo_block = f"""
    <title>{page_title}</title>
    <meta name="description" content="Explore {clean_name}, a professional web project developed by {DEV_INFO['name']}. Featuring advanced UI/UX design and modern web technologies.">
    <meta name="keywords" content="{clean_name}, {DEV_INFO['name']}, {DEV_INFO['website']}, Full-Stack Developer, Portfolio, Web Design, Morocco Developer">
    <meta name="author" content="{DEV_INFO['name']}">
    <link rel="canonical" href="https://{DEV_INFO['website']}/{project_name}/{os.path.basename(html_path)}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://{DEV_INFO['website']}/{project_name}/{os.path.basename(html_path)}">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="Professional web portal: {clean_name}. Designed and developed by {DEV_INFO['name']}.">
    <meta property="og:image" content="https://{DEV_INFO['website']}/{DEV_INFO['photo']}">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://{DEV_INFO['website']}/{project_name}/{os.path.basename(html_path)}">
    <meta property="twitter:title" content="{page_title}">
    <meta property="twitter:description" content="Professional web portal: {clean_name}. Designed and developed by {DEV_INFO['name']}.">
    <meta property="twitter:image" content="https://{DEV_INFO['website']}/{DEV_INFO['photo']}">

    <!-- GEO Tags -->
    <meta name="geo.region" content="MA" />
    <meta name="geo.placename" content="Morocco" />
    <meta name="geo.position" content="31.7917;-7.0926" />
    <meta name="ICBM" content="31.7917, -7.0926" />

    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "{DEV_INFO['name']}",
      "url": "https://{DEV_INFO['website']}",
      "email": "{DEV_INFO['email']}",
      "telephone": "{DEV_INFO['phone']}",
      "jobTitle": "Full-Stack Developer",
      "sameAs": [
        "{DEV_INFO['github']}",
        "{DEV_INFO['linkedin']}"
      ],
      "worksFor": {{
        "@type": "Organization",
        "name": "{DEV_INFO['website']}"
      }}
    }}
    </script>
    """
        if '</head>' in html:
            html = html.replace('</head>', f"{seo_block}\n</head>")

        # 4. HEADER BRANDING
        photo_html = f'<img src="{DEV_INFO["photo"]}" alt="{DEV_INFO["name"]}" class="w-8 h-8 rounded-full border-2 border-orange-500 object-cover">'
        html = re.sub(r'<(span|a)[^>]*class="[^"]*material-symbols-outlined[^"]*"[^>]*>(person|account_circle)</\1>', photo_html, html)

        # 5. FOOTER BRANDING (Perfected)
        footer_branding = f"""
    <div class="personal-footer" style="margin: 80px auto 40px; padding: 40px 20px; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; font-family: sans-serif; background: rgba(0,0,0,0.3); width: 100%; max-width: 1200px; border-radius: 24px; backdrop-filter: blur(10px); position: relative; z-index: 1000;">
        <img src="{DEV_INFO['photo']}" alt="{DEV_INFO['name']}" style="width: 80px; height: 80px; border-radius: 50%; border: 3px solid #ff6b00; margin: 0 auto 20px; box-shadow: 0 0 30px rgba(255,107,0,0.2);">
        <p style="color: #fff; font-size: 20px; margin-bottom: 8px; font-weight: 700; letter-spacing: 1px;">{DEV_INFO['name']}</p>
        <p style="color: rgba(255,255,255,0.5); font-size: 14px; margin-bottom: 24px; font-weight: 400;">Full-Stack Engineer & Digital Architect</p>
        
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">
            <a href="{DEV_INFO['github']}" target="_blank" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s; border: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; gap: 8px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.041-1.61-4.041-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                GitHub
            </a>
            <a href="{DEV_INFO['linkedin']}" target="_blank" style="color: #fff; text-decoration: none; background: #0077b5; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s; display: flex; align-items: center; gap: 8px;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
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
        
        # Finally, re-inject the branding at the very end of <body>
        if '</body>' in html:
            html = html.replace('</body>', f"{footer_branding}\n</body>")

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    except Exception as e:
        print(f"Error processing {html_path}: {e}")
        return False

def process_all_portals():
    base_dir = r"c:\Users\hsini\Desktop\34project\more"
    project_folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d not in ["scratch_restore", "zip"]]
    
    for folder in project_folders:
        project_path = os.path.join(base_dir, folder)
        files = [f for f in os.listdir(project_path) if f.endswith('.html')]
        
        for f in files:
            full_path = os.path.join(project_path, f)
            inject_seo(full_path, folder)
        print(f"Branding & SEO Optimized (v29 - Total Cleanup): {folder}")

if __name__ == "__main__":
    process_all_portals()
