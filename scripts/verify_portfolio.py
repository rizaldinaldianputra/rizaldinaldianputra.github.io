import os
import re

for html_file in ['portfolio.html', 'index.html']:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print(f"=== {html_file} ===")
    boxes = re.findall(r'<div class="portfolio_box">', content)
    print(f"Total portfolio_box items: {len(boxes)}")
    
    # Check all img src inside portfolio section
    imgs = re.findall(r'src="(img/portfolio/[^"]+)"', content)
    missing_imgs = [i for i in imgs if not os.path.exists(i)]
    print(f"Total img elements: {len(imgs)}, Missing: {len(missing_imgs)}")
    
    # Check all gallery hrefs
    gal_links = re.findall(r'class="img-gal[^"]*"[^>]*href="(img/portfolio/[^"]+)"', content)
    gal_links += re.findall(r'href="(img/portfolio/[^"]+)"[^>]*class="img-gal[^"]*"', content)
    missing_gal = [g for g in gal_links if not os.path.exists(g)]
    print(f"Total gallery links: {len(gal_links)}, Missing: {len(missing_gal)}")
    
    # Check videos
    videos = re.findall(r'data-video="(img/portfolio/[^"]+)"', content)
    missing_videos = [v for v in videos if not os.path.exists(v)]
    print(f"Total video links: {len(videos)}, Missing: {len(missing_videos)}")
    
    if missing_imgs or missing_gal or missing_videos:
        print("ERRORS FOUND:")
        if missing_imgs: print("  Missing imgs:", missing_imgs)
        if missing_gal: print("  Missing gal:", missing_gal)
        if missing_videos: print("  Missing videos:", missing_videos)
    else:
        print(">> SUCCESS: 100% verified! All assets exist and are properly linked.\n")

