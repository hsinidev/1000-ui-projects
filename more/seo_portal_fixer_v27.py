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

        # 1. CLEANUP PREVIOUS ATTEMPTS (Safely)
        html = re.sub(r'<!-- JSON-LD Schema -->.*?({.*?})?.*?</script>', '', html, flags=re.DOTALL)
        html = re.sub(r'<title>.*?</title>', '', html, flags=re.DOTALL)
        html = re.sub(r'<meta name="description" content=".*?">', '', html)
        html = re.sub(r'<meta name="keywords" content=".*?">', '', html)
        html = re.sub(r'<meta name="author" content=".*?">', '', html)
        html = re.sub(r'<!-- Open Graph / Facebook -->.*?<!-- Twitter -->', '', html, flags=re.DOTALL)
        html = re.sub(r'<!-- Twitter -->.*?<!-- GEO Tags -->', '', html, flags=re.DOTALL)
        html = re.sub(r'<!-- GEO Tags -->.*?<!-- JSON-LD Schema -->', '', html, flags=re.DOTALL)
        html = re.sub(r'<div class="personal-footer".*?</div>', '', html, flags=re.DOTALL)

        # 2. PREPARE NEW SEO BLOCK
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

        # 3. HEADER BRANDING
        photo_html = f'<img src="{DEV_INFO["photo"]}" alt="{DEV_INFO["name"]}" class="w-8 h-8 rounded-full border-2 border-orange-500 object-cover">'
        html = re.sub(r'<(span|a)[^>]*class="[^"]*material-symbols-outlined[^"]*"[^>]*>(person|account_circle)</\1>', photo_html, html)

        # 4. FOOTER BRANDING (Updated with GitHub & LinkedIn)
        footer_branding = f"""
    <div class="personal-footer" style="margin: 80px auto 40px; padding: 40px 20px; border-top: 1px solid rgba(255,255,255,0.05); text-align: center; font-family: sans-serif; background: rgba(0,0,0,0.3); width: 100%; max-width: 1200px; border-radius: 24px; backdrop-filter: blur(10px);">
        <img src="{DEV_INFO['photo']}" alt="{DEV_INFO['name']}" style="width: 80px; height: 80px; border-radius: 50%; border: 3px solid #ff6b00; margin: 0 auto 20px; box-shadow: 0 0 30px rgba(255,107,0,0.2);">
        <p style="color: #fff; font-size: 20px; margin-bottom: 8px; font-weight: 700; letter-spacing: 1px;">{DEV_INFO['name']}</p>
        <p style="color: rgba(255,255,255,0.5); font-size: 14px; margin-bottom: 24px; font-weight: 400;">Full-Stack Engineer & Digital Architect</p>
        
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;">
            <a href="{DEV_INFO['github']}" target="_blank" style="color: #fff; text-decoration: none; background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s; border: 1px solid rgba(255,255,255,0.1);">GitHub</a>
            <a href="{DEV_INFO['linkedin']}" target="_blank" style="color: #fff; text-decoration: none; background: #0077b5; padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 600; transition: all 0.3s;">LinkedIn</a>
        </div>

        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 30px; font-size: 13px; color: rgba(255,255,255,0.7);">
            <a href="https://{DEV_INFO['website']}" style="color: #ff6b00; text-decoration: none; font-weight: 600; border-bottom: 1px solid rgba(255,107,0,0.3); padding-bottom: 2px;">{DEV_INFO['website']}</a>
            <a href="mailto:{DEV_INFO['email']}" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2px;">{DEV_INFO['email']}</a>
            <a href="tel:{DEV_INFO['phone']}" style="color: inherit; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2px;">{DEV_INFO['phone']}</a>
        </div>
        <p style="margin-top: 40px; color: rgba(255,255,255,0.15); font-size: 11px; letter-spacing: 2px; text-transform: uppercase;">© 2024 HSINI.DEV | All Rights Reserved</p>
    </div>
    """
        
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
        print(f"Branding & SEO Optimized (v27 - Socials): {folder}")

if __name__ == "__main__":
    process_all_portals()
