document.addEventListener("DOMContentLoaded", () => {
    // 1. Custom Cursor Functionality
    const cursor = document.querySelector('.cursor');
    if (cursor) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Add hover effect to interactive elements
        const interactiveElemenets = document.querySelectorAll('a, button, .portfolio_box, .feature_item');
        interactiveElemenets.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.classList.add('hovered');
            });
            el.addEventListener('mouseleave', () => {
                cursor.classList.remove('hovered');
            });
        });
    }

    // Register ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // 2. Hero Banner Animations (On Load)
    const heroTl = gsap.timeline({ defaults: { ease: "power3.out", duration: 1 } });
    
    // Animate texts staggering up
    heroTl.from('.banner_content h3', { y: 50, opacity: 0, delay: 0.2 })
          .from('.banner_content h1', { y: 50, opacity: 0 }, "-=0.7")
          .from('.banner_content h5', { y: 50, opacity: 0 }, "-=0.7")
          .from('.banner_content .d-flex a', { y: 30, opacity: 0, stagger: 0.2 }, "-=0.6")
          .from('.home_right_img img', { x: 50, opacity: 0, duration: 1.5, ease: "slow" }, "-=1");

    // 3. Parallax Image Effects
    gsap.to('.home_right_img img', {
        yPercent: 30,
        ease: "none",
        scrollTrigger: {
            trigger: ".home_banner_area",
            start: "top top",
            end: "bottom top",
            scrub: true
        }
    });

    gsap.to('.about_img img', {
        yPercent: 20,
        ease: "none",
        scrollTrigger: {
            trigger: ".about_area",
            start: "top bottom",
            end: "bottom top",
            scrub: true
        }
    });

    // 4. About Section Reveal
    gsap.from('.about_area .main_title h2, .about_area .main_title p, .about_area .primary_btn', {
        y: 50,
        opacity: 0,
        stagger: 0.2,
        duration: 1,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".about_area",
            start: "top 75%",
        }
    });

    // 5. Brands stagger
    gsap.from('.single-brand-item img', {
        scale: 0.5,
        opacity: 0,
        stagger: 0.05,
        duration: 0.8,
        ease: "back.out(1.7)",
        scrollTrigger: {
            trigger: ".brand_area",
            start: "top 85%"
        }
    });

    // 6. Services / Features Cards
    gsap.from('.feature_item', {
        y: 100,
        opacity: 0,
        stagger: 0.15,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: {
            trigger: ".features_area",
            start: "top 70%"
        }
    });

    // 7. Portfolio Items (Batch reveal to support isotope filter updates)
    gsap.from('.portfolio_box', {
        scale: 0.9,
        opacity: 0,
        stagger: 0.04,
        duration: 0.6,
        ease: "power2.out",
        scrollTrigger: {
            trigger: ".portfolio_area",
            start: "top 65%"
        }
    });

    // 8. Testimonials Fade
    gsap.from('.testimonial_area .main_title', {
        y: 40,
        opacity: 0,
        duration: 1,
        scrollTrigger: {
            trigger: ".testimonial_area",
            start: "top 80%"
        }
    });

    // Smooth scroll navigation for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target) {
                gsap.to(window, {duration: 1, scrollTo: target.offsetTop, ease: "power2.inOut"});
            }
        });
    });
});
