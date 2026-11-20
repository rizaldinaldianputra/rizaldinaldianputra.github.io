"""
Script otomatis untuk scan folder img/portfolio dan update index.html & portfolio.html
Jalankan perintah: python scripts/generate_portfolio.py
"""

import os
import re
import html

BASE_DIR = 'img/portfolio'

PROJECT_META = {
    'Zelixa-School': {
        'title': 'Zelixa School Management',
        'subtitle': 'Complete School Ecosystem: Finance, Principal, Student, Teacher & TU Dashboards',
        'category_classes': 'all system web',
        'badge_cat': 'EdTech ERP',
        'cover': 'Finance.png'
    },
    'zelikas': {
        'title': 'Zelikas Finance & Kasir',
        'subtitle': 'Smart Financial Tracking & POS Cashier App for Mobile & Tablet',
        'category_classes': 'all mobile system',
        'badge_cat': 'Mobile & Tablet',
        'cover': 'dashboard.jpeg'
    },
    'Zelivira': {
        'title': 'Zelivira POS & Order',
        'subtitle': 'Modern Food, Beverage & Retail POS for Mobile and Tablet Devices',
        'category_classes': 'all mobile system',
        'badge_cat': 'POS & Tablet',
        'cover': 'LOGINZEL.jpeg'
    },
    'zelixa pos': {
        'title': 'Zelixa POS Multi-platform',
        'subtitle': 'Next-Gen Point of Sale for Retail & Restaurant Management',
        'category_classes': 'all mobile system',
        'badge_cat': 'POS System',
        'cover': 'WhatsApp Image 2026-07-29 at 15.07.31.jpeg'
    },
    'Zelixa Quran': {
        'title': 'Zelixa Quran',
        'subtitle': 'Digital Al-Quran, Prayer Times, Qibla Direction, Daily Duas & Tasbih',
        'category_classes': 'all mobile',
        'badge_cat': 'Mobile App',
        'cover': 'home.jpeg'
    },
    'ALQURAN': {
        'title': 'Al-Quran Mobile App',
        'subtitle': 'Digital Holy Quran Reader & Audio Recitation App',
        'category_classes': 'all mobile',
        'badge_cat': 'Mobile App',
        'cover': 'Mobile App Screen Mockup, Floating (1).png'
    },
    'WA GATEWAY': {
        'title': 'WhatsApp Gateway Platform',
        'subtitle': 'Multi-Device WA API, Message Automation & Broadcast Dashboard',
        'category_classes': 'all system web',
        'badge_cat': 'API & Gateway',
        'cover': 'screencapture-localhost-3000-dashboard-2026-06-24-14_03_00.png'
    },
    'Cosmic ERP': {
        'title': 'Cosmic ERP System',
        'subtitle': 'Enterprise Resource Planning & Business Management Platform',
        'category_classes': 'all system web',
        'badge_cat': 'ERP System',
        'cover': '1771493963443.jpg'
    },
    'HRSYSTEM MANYALA': {
        'title': 'HRIS Manyala Group',
        'subtitle': 'Employee Database, Payroll, Leave & Attendance System',
        'category_classes': 'all system web',
        'badge_cat': 'HRIS System',
        'cover': 'HRIS.png'
    },
    'HRSYSTEM SINAR12': {
        'title': 'HR System & Mobile Sinar12',
        'subtitle': 'Corporate HR Web Portal & Mobile Attendance App (CMM Group)',
        'category_classes': 'all system mobile',
        'badge_cat': 'HRIS & Mobile',
        'cover': 'hrsystem-web.jpg'
    },
    'CRM CHAT': {
        'title': 'Fast Chat Meja Bantu',
        'subtitle': 'Omnichannel Customer Support & Live CRM Chat System',
        'category_classes': 'all system web',
        'badge_cat': 'CRM & Chat',
        'cover': 'fastchat.png'
    },
    'POS SINAR12': {
        'title': 'Point of Sale Sinar12',
        'subtitle': 'Retail Cashier, Product Inventory & POS System',
        'category_classes': 'all system',
        'badge_cat': 'POS System',
        'cover': 'pos.jpg'
    },
    'smart schol ampuri': {
        'title': 'Smart School Ampuri',
        'subtitle': 'Integrated Digital School & Academic Management System',
        'category_classes': 'all mobile system',
        'badge_cat': 'EdTech / Mobile',
        'cover': 'WhatsApp Image 2026-06-24 at 15.09.51.jpeg'
    },
    'amphrui': {
        'title': 'Amphuri Umrah Travel',
        'subtitle': 'Umrah & Hajj Tour Travel Management Web System',
        'category_classes': 'all web system',
        'badge_cat': 'Web / System',
        'cover': 'Screenshot 2026-06-24 151341.png'
    },
    'ECOMMERCE SINAR1': {
        'title': 'E-Commerce Sinar12',
        'subtitle': 'Official Online Store & Reseller Distribution Platform',
        'category_classes': 'all web',
        'badge_cat': 'E-Commerce',
        'cover': 'ecommerce.jpg'
    },
    'ECOMMERCE ERICO': {
        'title': 'Whell World E-Commerce',
        'subtitle': 'Automotive Wheels & Tires Online Shopping Platform',
        'category_classes': 'all web',
        'badge_cat': 'E-Commerce',
        'cover': 'whell.png'
    },
    'sasienala ecommerce': {
        'title': 'Sasienala Fashion Store',
        'subtitle': 'Exclusive Fashion, Hijab & Lifestyle Online Shopping',
        'category_classes': 'all web',
        'badge_cat': 'E-Commerce',
        'cover': 'sasienala.png'
    },
    'GTA CONSTRUACTION': {
        'title': 'GTA Construction',
        'subtitle': 'General Contractor, Architecture & Engineering Corporate Website',
        'category_classes': 'all web',
        'badge_cat': 'Corporate Web',
        'cover': 'screencapture-gtaconstruction-co-id-2026-06-24-15_18_01.png'
    },
    'HAVEN KOS': {
        'title': 'Haven Kos Living',
        'subtitle': 'Premium Boarding House & Property Rental Web Platform',
        'category_classes': 'all web',
        'badge_cat': 'Web Platform',
        'cover': 'screencapture-haven-co-id-2026-06-24-15_16_57.png'
    },
    'MY BALIFRIENDZ': {
        'title': 'My Bali Friendz',
        'subtitle': 'Bali Tour Packages, Activities & Travel Booking Portal',
        'category_classes': 'all web',
        'badge_cat': 'Travel Portal',
        'cover': 'screencapture-mybalifriendz-co-2026-06-24-14_10_30.png'
    },
    'zelixa tech': {
        'title': 'Zelixa Tech Company Profile',
        'subtitle': 'Modern Software House, App Development & IT Agency Website',
        'category_classes': 'all web',
        'badge_cat': 'Corporate Web',
        'cover': 'Screenshot 2026-06-26 100033.png'
    },
    'Ojek Online': {
        'title': 'Ojek Online App',
        'subtitle': 'Ride Hailing, Food & On-Demand Delivery Mobile App',
        'category_classes': 'all mobile',
        'badge_cat': 'Mobile App',
        'cover': '1771483526045.jpg'
    },
    'BARBERSHOP': {
        'title': 'Barbershop App',
        'subtitle': 'Haircut Booking, Hairstylist & Grooming Mobile Platform',
        'category_classes': 'all mobile',
        'badge_cat': 'Mobile App',
        'cover': 'barber.png'
    },
    'TICKETING': {
        'title': 'Ticketing SR12',
        'subtitle': 'Anniversary Event Registration & QR Code Ticket Scanner',
        'category_classes': 'all system web',
        'badge_cat': 'Event & Ticket',
        'cover': 'ticketing.jpg'
    }
}

VIDEO_MODAL_HTML = '''
	<!-- Portfolio Video Modal -->
	<div class="modal fade" id="portfolioVideoModal" tabindex="-1" role="dialog" aria-labelledby="portfolioVideoModalLabel" aria-hidden="true">
		<div class="modal-dialog modal-dialog-centered modal-lg" role="document">
			<div class="modal-content" style="background: #111; border: 1px solid #333; border-radius: 12px; overflow: hidden;">
				<div class="modal-header" style="border-bottom: 1px solid #222; padding: 15px 20px;">
					<h5 class="modal-title text-white" id="portfolioVideoModalLabel" style="font-size: 16px; font-weight: 600;">Project Demo Video</h5>
					<button type="button" class="close text-white" data-dismiss="modal" aria-label="Close" style="opacity: 0.8; outline: none;">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body p-0 text-center" style="background: #000;">
					<video id="portfolioModalVideo" controls playsinline style="width: 100%; max-height: 75vh; outline: none; display: block; margin: 0 auto;"></video>
				</div>
			</div>
		</div>
	</div>
'''

def scan_projects():
    projects = []
    # Scan configured folders first in specified order
    folders = list(PROJECT_META.keys())
    
    # Also discover any newly added folders not in meta
    for d in sorted(os.listdir(BASE_DIR)):
        if os.path.isdir(os.path.join(BASE_DIR, d)) and d not in folders:
            folders.append(d)

    for folder in folders:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(folder_path):
            continue

        d = PROJECT_META.get(folder, {
            'title': folder.title(),
            'subtitle': 'Project Portfolio Showcase',
            'category_classes': 'all web',
            'badge_cat': 'Project',
            'cover': ''
        })

        images = []
        videos = []
        for root, _, files in os.walk(folder_path):
            for f in sorted(files):
                ext = os.path.splitext(f)[1].lower()
                rel_path = os.path.relpath(os.path.join(root, f), '.').replace('\\', '/')
                if ext in ['.png', '.jpg', '.jpeg', '.webp']:
                    clean_name = os.path.splitext(f)[0]
                    images.append((rel_path, clean_name))
                elif ext in ['.mp4', '.mov']:
                    videos.append((rel_path, f))

        cover_rel = os.path.join(BASE_DIR, folder, d['cover']).replace('\\', '/')
        if not os.path.exists(cover_rel):
            cover_rel = images[0][0] if images else ""

        cover_item = next((img for img in images if img[0] == cover_rel), None)
        other_items = [img for img in images if img[0] != cover_rel]
        sorted_images = ([cover_item] if cover_item else []) + other_items

        projects.append({
            'folder': folder,
            'title': d['title'],
            'subtitle': d['subtitle'],
            'category_classes': d['category_classes'],
            'badge_cat': d['badge_cat'],
            'cover': cover_rel,
            'images': sorted_images,
            'videos': videos
        })

    # Add System ERP Sinar12 from root if exists
    erp_path = 'img/portfolio/erp.jpg'
    if os.path.exists(erp_path):
        projects.append({
            'folder': 'Sinar12 ERP',
            'title': 'System ERP Sinar12',
            'subtitle': 'Integrated Enterprise Resource Planning for Supply & Retail',
            'category_classes': 'all system web',
            'badge_cat': 'ERP System',
            'cover': erp_path,
            'images': [(erp_path, 'ERP Dashboard')],
            'videos': []
        })

    return projects

def build_grid_html(projects):
    html_cards = []
    for p in projects:
        title_esc = html.escape(p['title'], quote=True)
        sub_esc = html.escape(p['subtitle'], quote=True)
        cat_classes = p['category_classes']
        badge_cat = html.escape(p['badge_cat'], quote=True)
        cover_url = p['cover']

        img_count = len(p['images'])
        has_video = len(p['videos']) > 0

        badge_html = ""
        if has_video:
            badge_html = f'<span class="portfolio_badge"><i class="fa fa-play-circle"></i> Video + {img_count} Screens</span>'
        elif img_count > 1:
            badge_html = f'<span class="portfolio_badge"><i class="fa fa-clone"></i> {img_count} Screens</span>'

        hidden_imgs_html = []
        for i, (img_url, img_name) in enumerate(p['images']):
            if i == 0:
                continue
            item_title = f"{title_esc} - {html.escape(img_name, quote=True)}"
            hidden_imgs_html.append(f'<a href="{img_url}" class="img-gal d-none" title="{item_title}"></a>')
        hidden_imgs_str = "\n\t\t\t\t\t\t\t\t".join(hidden_imgs_html)
        if hidden_imgs_str:
            hidden_imgs_str = "\n\t\t\t\t\t\t\t\t" + hidden_imgs_str

        video_link = ""
        if has_video:
            v_url = p['videos'][0][0]
            v_title = f"{title_esc} Demo Video"
            video_link = f'\n\t\t\t\t\t\t\t\t<div><a href="javascript:void(0)" class="video-modal-trigger video-btn-link" data-video="{v_url}" data-title="{v_title}"><i class="fa fa-play-circle"></i> Watch Video Demo</a></div>'

        card = f'''\t\t\t\t\t<div class="col-lg-4 col-md-6 {cat_classes}">
\t\t\t\t\t\t<div class="portfolio_box">
\t\t\t\t\t\t\t<div class="single_portfolio">
\t\t\t\t\t\t\t\t<span class="portfolio_category_badge">{badge_cat}</span>
\t\t\t\t\t\t\t\t{badge_html}
\t\t\t\t\t\t\t\t<div class="portfolio_thumb_wrapper">
\t\t\t\t\t\t\t\t\t<div class="shimmer_loader"></div>
\t\t\t\t\t\t\t\t\t<img class="img-fluid w-100 portfolio_img_lazy" src="{cover_url}" alt="{title_esc}" loading="lazy" decoding="async" onload="this.classList.add(\'loaded\');">
\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t<div class="overlay"></div>
\t\t\t\t\t\t\t\t<a href="{cover_url}" class="img-gal" title="{title_esc}">
\t\t\t\t\t\t\t\t\t<div class="icon">
\t\t\t\t\t\t\t\t\t\t<span class="lnr lnr-cross"></span>
\t\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t\t</a>{hidden_imgs_str}
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t<div class="short_info">
\t\t\t\t\t\t\t\t<h4><a href="javascript:void(0)" class="portfolio_title_btn">{title_esc}</a></h4>
\t\t\t\t\t\t\t\t<p>{sub_esc}</p>{video_link}
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>'''
        html_cards.append(card)

    return "\n".join(html_cards)

def update_html_files():
    projects = scan_projects()
    grid_snippet = build_grid_html(projects)

    filter_section = f'''            <div class="filters portfolio-filter">
                <ul>
                    <li class="active" data-filter="*">All</li>
                    <li data-filter=".mobile">Mobile App</li>
                    <li data-filter=".web">Web Development</li>
                    <li data-filter=".system">ERP & System</li>
                </ul>
            </div>
    
            <div class="filters-content">
				<div class="row portfolio-grid justify-content-center">
{grid_snippet}
				</div>
			</div>'''

    # Update portfolio.html
    if os.path.exists('portfolio.html'):
        with open('portfolio.html', 'r', encoding='utf-8') as f:
            p_content = f.read()
        p_pattern = re.compile(r'<div class="filters portfolio-filter">.*?</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
        if p_pattern.search(p_content):
            p_content_new = p_pattern.sub(filter_section + "\n        </div>\n    </section>", p_content)
            if 'id="portfolioVideoModal"' not in p_content_new:
                p_content_new = p_content_new.replace('</body>', VIDEO_MODAL_HTML + '\n</body>')
            with open('portfolio.html', 'w', encoding='utf-8') as f:
                f.write(p_content_new)
            print("[OK] portfolio.html updated successfully!")

    # Update index.html
    if os.path.exists('index.html'):
        with open('index.html', 'r', encoding='utf-8') as f:
            idx_content = f.read()
        idx_pattern = re.compile(r'<section class="portfolio_area[^"]*" id="portfolio">.*?</section>\s*<!--================End Portfolio Area =================-->', re.DOTALL)
        if idx_pattern.search(idx_content):
            new_idx_section = f'''<section class="portfolio_area section_gap_top" id="portfolio">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="main_title text-left">
                        <h2>quality work <br>
                            Recently done project </h2>
                    </div>
                </div>
            </div>
{filter_section}
        </div>
    </section>
	<!--================End Portfolio Area =================-->'''
            idx_content_new = idx_pattern.sub(new_idx_section, idx_content)
            if 'id="portfolioVideoModal"' not in idx_content_new:
                idx_content_new = idx_content_new.replace('</body>', VIDEO_MODAL_HTML + '\n</body>')
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(idx_content_new)
            print("[OK] index.html updated successfully!")

    print(f"\nTotal projects integrated: {len(projects)}")

if __name__ == '__main__':
    update_html_files()
