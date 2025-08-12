
/* ========================================
   ADVANCED ANIMATION CONTROLLERS
   Philip Wright Professional Portfolio
   ======================================== */

class AnimationController {
    constructor() {
        this.init();
    }
    
    init() {
        this.setupScrollAnimations();
        this.setupNavigationEffects();
        this.setupCounterAnimations();
        this.setupParallaxEffects();
        this.setupProgressBars();
        this.setupTypewriterEffect();
        this.setupImageReveal();
    }
    
    // Scroll-based animations
    setupScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    
                    // Handle staggered items
                    if (entry.target.classList.contains('stagger-container')) {
                        const items = entry.target.querySelectorAll('.stagger-item');
                        items.forEach((item, index) => {
                            setTimeout(() => {
                                item.classList.add('visible');
                            }, index * 100);
                        });
                    }
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        // Observe all elements with animation classes
        document.querySelectorAll('.animate-on-scroll, .stagger-container, .image-reveal').forEach(el => {
            observer.observe(el);
        });
    }
    
    // Navigation scroll effects
    setupNavigationEffects() {
        let lastScrollY = window.scrollY;
        
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            const nav = document.querySelector('nav');
            
            if (nav) {
                // Add scrolled class
                if (scrollY > 100) {
                    nav.classList.add('scrolled');
                } else {
                    nav.classList.remove('scrolled');
                }
                
                // Hide/show nav based on scroll direction
                if (scrollY > lastScrollY && scrollY > 500) {
                    nav.style.transform = 'translateY(-100%)';
                } else {
                    nav.style.transform = 'translateY(0)';
                }
            }
            
            lastScrollY = scrollY;
        });
    }
    
    // Animated counters
    setupCounterAnimations() {
        const counters = document.querySelectorAll('.counter');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const finalValue = parseInt(target.dataset.count) || 100;
                    
                    target.classList.add('animate');
                    
                    let current = 0;
                    const increment = finalValue / 50;
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= finalValue) {
                            current = finalValue;
                            clearInterval(timer);
                        }
                        target.textContent = Math.floor(current);
                    }, 40);
                    
                    observer.unobserve(target);
                }
            });
        });
        
        counters.forEach(counter => observer.observe(counter));
    }
    
    // Parallax scrolling
    setupParallaxEffects() {
        const parallaxElements = document.querySelectorAll('.parallax-element');
        
        if (parallaxElements.length > 0) {
            window.addEventListener('scroll', () => {
                const scrolled = window.pageYOffset;
                
                parallaxElements.forEach(element => {
                    const rate = scrolled * (element.dataset.rate || -0.5);
                    element.style.transform = `translateY(${rate}px)`;
                });
            });
        }
    }
    
    // Progress bar animations
    setupProgressBars() {
        const progressBars = document.querySelectorAll('.progress-fill');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const progressFill = entry.target;
                    const percentage = progressFill.dataset.percentage || '100';
                    
                    progressFill.style.width = percentage + '%';
                    progressFill.classList.add('animate');
                    
                    observer.unobserve(progressFill);
                }
            });
        });
        
        progressBars.forEach(bar => observer.observe(bar));
    }
    
    // Typewriter effect
    setupTypewriterEffect() {
        const typewriterElements = document.querySelectorAll('.typewriter');
        
        typewriterElements.forEach(element => {
            const text = element.textContent;
            element.textContent = '';
            element.style.width = '0';
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        this.typeText(element, text);
                        observer.unobserve(element);
                    }
                });
            });
            
            observer.observe(element);
        });
    }
    
    typeText(element, text) {
        let index = 0;
        const speed = 100;
        
        function type() {
            if (index < text.length) {
                element.textContent += text.charAt(index);
                index++;
                setTimeout(type, speed);
            }
        }
        
        // Animate width
        element.style.width = '100%';
        setTimeout(type, 500);
    }
    
    // Image reveal effect
    setupImageReveal() {
        const imageElements = document.querySelectorAll('.image-reveal');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                    observer.unobserve(entry.target);
                }
            });
        });
        
        imageElements.forEach(img => observer.observe(img));
    }
    
    // Smooth scroll to sections
    static smoothScrollTo(targetId) {
        const target = document.getElementById(targetId);
        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    }
    
    // Loading animation
    static showLoading() {
        const loader = document.createElement('div');
        loader.className = 'loading-spinner';
        loader.style.position = 'fixed';
        loader.style.top = '50%';
        loader.style.left = '50%';
        loader.style.transform = 'translate(-50%, -50%)';
        loader.style.zIndex = '9999';
        document.body.appendChild(loader);
        
        return loader;
    }
    
    static hideLoading(loader) {
        if (loader && loader.parentNode) {
            loader.remove();
        }
    }
}

// Initialize animations when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AnimationController();
});

// Utility functions for manual animation triggering
window.AnimationUtils = {
    fadeIn: (element, duration = 500) => {
        element.style.opacity = '0';
        element.style.transition = `opacity ${duration}ms ease`;
        
        setTimeout(() => {
            element.style.opacity = '1';
        }, 10);
    },
    
    slideInFromLeft: (element, duration = 500) => {
        element.style.transform = 'translateX(-100%)';
        element.style.transition = `transform ${duration}ms cubic-bezier(0.25, 0.46, 0.45, 0.94)`;
        
        setTimeout(() => {
            element.style.transform = 'translateX(0)';
        }, 10);
    },
    
    bounceIn: (element, duration = 600) => {
        element.style.transform = 'scale(0)';
        element.style.transition = `transform ${duration}ms cubic-bezier(0.68, -0.55, 0.265, 1.55)`;
        
        setTimeout(() => {
            element.style.transform = 'scale(1)';
        }, 10);
    }
};

// Performance optimization
if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
        // Preload critical animations
        const criticalElements = document.querySelectorAll('.hero, nav, .cta-button');
        criticalElements.forEach(el => {
            el.style.willChange = 'transform, opacity';
        });
    });
}
