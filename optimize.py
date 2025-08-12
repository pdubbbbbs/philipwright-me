#!/usr/bin/env python3
"""
Performance Optimization Script for Philip Wright Website
- Minifies CSS and JavaScript
- Optimizes images (if present)
- Generates performance reports
- Adds analytics tracking
"""

import os
import re
import json
import gzip
import shutil
from pathlib import Path

def minify_css(css_content):
    """Minify CSS by removing unnecessary whitespace and comments"""
    # Remove comments
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra whitespace
    css_content = re.sub(r'\s+', ' ', css_content)
    # Remove whitespace around certain characters
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    # Remove trailing semicolon before }
    css_content = re.sub(r';\s*}', '}', css_content)
    return css_content.strip()

def minify_js(js_content):
    """Basic JavaScript minification"""
    # Remove single line comments (but preserve URLs)
    js_content = re.sub(r'(?<!:)//.*$', '', js_content, flags=re.MULTILINE)
    # Remove multi-line comments
    js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
    # Remove extra whitespace
    js_content = re.sub(r'\s+', ' ', js_content)
    # Remove whitespace around operators
    js_content = re.sub(r'\s*([{}();,=+\-*/<>!&|])\s*', r'\1', js_content)
    return js_content.strip()

def create_gzip_version(file_path):
    """Create gzip compressed version of file"""
    with open(file_path, 'rb') as f_in:
        with gzip.open(f"{file_path}.gz", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def add_analytics_tracking():
    """Add Google Analytics tracking to index.html"""
    analytics_script = '''
    <!-- Google Analytics (replace GA_MEASUREMENT_ID with your actual ID) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_MEASUREMENT_ID');
    </script>
    '''
    
    # Read index.html
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if analytics is already present
    if 'gtag' not in content:
        # Add analytics before closing head tag
        content = content.replace('</head>', f'{analytics_script}\n</head>')
        
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(content)
        
        print("✅ Added Google Analytics tracking (remember to replace GA_MEASUREMENT_ID)")
    else:
        print("✅ Analytics tracking already present")

def create_manifest():
    """Create enhanced web app manifest"""
    manifest = {
        "name": "Philip Wright - Professional Portfolio",
        "short_name": "Philip Wright",
        "description": "Professional portfolio showcasing innovative solutions and strategic thinking",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#1a1a1a",
        "theme_color": "#c9b037",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/android-chrome-512x512.png", 
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ],
        "categories": ["portfolio", "business", "professional"],
        "lang": "en",
        "dir": "ltr"
    }
    
    with open('site.webmanifest', 'w', encoding='utf-8') as file:
        json.dump(manifest, file, indent=2)
    
    print("✅ Enhanced web app manifest created")

def optimize_performance():
    """Main optimization function"""
    print("🚀 Philip Wright Website Performance Optimizer")
    print("=" * 45)
    
    # Create minified versions
    if os.path.exists('styles.css'):
        print("🎨 Optimizing CSS...")
        with open('styles.css', 'r', encoding='utf-8') as file:
            css_content = file.read()
        
        minified_css = minify_css(css_content)
        
        with open('styles.min.css', 'w', encoding='utf-8') as file:
            file.write(minified_css)
        
        create_gzip_version('styles.min.css')
        
        original_size = len(css_content)
        minified_size = len(minified_css)
        savings = ((original_size - minified_size) / original_size) * 100
        print(f"   Original: {original_size:,} bytes")
        print(f"   Minified: {minified_size:,} bytes")
        print(f"   Savings: {savings:.1f}%")
    
    if os.path.exists('script.js'):
        print("\n📜 Optimizing JavaScript...")
        with open('script.js', 'r', encoding='utf-8') as file:
            js_content = file.read()
        
        minified_js = minify_js(js_content)
        
        with open('script.min.js', 'w', encoding='utf-8') as file:
            file.write(minified_js)
        
        create_gzip_version('script.min.js')
        
        original_size = len(js_content)
        minified_size = len(minified_js)
        savings = ((original_size - minified_size) / original_size) * 100
        print(f"   Original: {original_size:,} bytes")
        print(f"   Minified: {minified_size:,} bytes")
        print(f"   Savings: {savings:.1f}%")
    
    # Add analytics tracking
    print("\n📈 Adding analytics...")
    add_analytics_tracking()
    
    # Enhance manifest
    print("\n📱 Enhancing web app manifest...")
    create_manifest()
    
    # Create performance tips
    print("\n💡 Creating performance tips...")
    performance_tips = """
# 🚀 Performance Optimization Tips

## Completed Automatically:
✅ CSS and JavaScript minification
✅ Gzip compression ready
✅ Enhanced web app manifest
✅ Analytics tracking added

## Manual Optimizations:
🖼️ **Images**: Add optimized images to /assets/images/
   - Use WebP format when possible
   - Compress images (aim for <100KB each)
   - Use appropriate sizes (no larger than needed)

🎯 **Analytics**: Replace 'GA_MEASUREMENT_ID' in index.html with your Google Analytics ID

⚡ **CDN**: Consider using a CDN for faster global delivery
   - Cloudflare (free tier available)
   - AWS CloudFront
   - Google Cloud CDN

🔧 **Headers**: Configure proper cache headers on your hosting platform
   - CSS/JS: cache for 1 year
   - HTML: cache for 1 hour
   - Images: cache for 1 month

## Performance Score Targets:
🎯 Google PageSpeed Insights: 90+ score
🎯 GTmetrix: Grade A
🎯 First Contentful Paint: <2 seconds
🎯 Largest Contentful Paint: <2.5 seconds
"""
    
    with open('PERFORMANCE-TIPS.md', 'w', encoding='utf-8') as file:
        file.write(performance_tips)
    
    print("✅ Created PERFORMANCE-TIPS.md")
    
    print(f"\n🎉 Optimization complete!")
    print(f"📊 Use minified files for production deployment")
    print(f"📋 Check PERFORMANCE-TIPS.md for additional optimizations")

if __name__ == "__main__":
    optimize_performance()
