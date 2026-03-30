document.addEventListener('DOMContentLoaded', () => {
    // === Mobile Menu Toggle ===
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    // Close mobile menu on link click
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });

    // === Sticky Navbar Effect ===
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled', 'py-1');
            navbar.classList.remove('py-3');
            // Update text colors for visibility if needed
            navbar.querySelector('.text-brand-100')?.classList.replace('text-brand-100', 'text-brand-900');
        } else {
            navbar.classList.remove('scrolled', 'py-1');
            navbar.classList.add('py-3');
        }
    });

    // Trigger scroll event on load to set initial state
    window.dispatchEvent(new Event('scroll'));

    // === Smooth Scrolling for Anchor Links ===
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerOffset = 80; // Height of floating navbar
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // === Counter Animation for Stats ===
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // The lower the slower

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 10);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
    };

    // Intersection Observer to trigger counter animation when in view
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    let animationTriggered = false;

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationTriggered) {
                animateCounters();
                animationTriggered = true;
                observer.disconnect(); // Only animate once
            }
        });
    }, observerOptions);

    const statsSection = document.getElementById('why-us');
    if (statsSection) {
        observer.observe(statsSection);
    }
});
