#!/bin/bash

# 🚀 Professional Website Deployment Script
# Philip Wright Personal Website
# Multiple hosting platform deployment options

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Philip Wright Website Deployment Script${NC}"
echo -e "${BLUE}===========================================${NC}"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to deploy to GitHub Pages
deploy_github() {
    echo -e "${YELLOW}📤 Deploying to GitHub Pages...${NC}"
    
    if ! command_exists git; then
        echo -e "${RED}❌ Git is not installed${NC}"
        exit 1
    fi
    
    # Check if we're in a git repository
    if [ ! -d .git ]; then
        echo -e "${YELLOW}🔧 Initializing Git repository...${NC}"
        git init
        git remote add origin https://github.com/pdubbbbbs/philipwright-me.git
    fi
    
    # Add all files
    git add .
    
    # Commit with timestamp
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    git commit -m "🚀 Website update: $TIMESTAMP

✨ Professional website deployment
📱 Mobile-responsive design
🎬 Video integration ready
🔍 SEO optimized
⚡ Performance optimized"
    
    # Push to main branch
    git branch -M main
    echo -e "${GREEN}✅ Ready to push to GitHub!${NC}"
    echo -e "${YELLOW}📋 Please run: git push -u origin main${NC}"
    echo -e "${YELLOW}🌐 Then enable Pages in GitHub repository settings${NC}"
}

# Function to deploy to Netlify
deploy_netlify() {
    echo -e "${YELLOW}📤 Preparing for Netlify deployment...${NC}"
    
    # Create netlify.toml for configuration
    cat > netlify.toml << EOF
[build]
  publish = "."

[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "*.js"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[headers]]
  for = "*.css"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
EOF
    
    echo -e "${GREEN}✅ Created netlify.toml configuration${NC}"
    echo -e "${YELLOW}📋 Manual steps:${NC}"
    echo -e "   1. Go to https://app.netlify.com/"
    echo -e "   2. Drag and drop this entire folder"
    echo -e "   3. Your site will be live instantly!"
}

# Function to deploy to Vercel
deploy_vercel() {
    echo -e "${YELLOW}📤 Preparing for Vercel deployment...${NC}"
    
    # Create vercel.json for configuration
    cat > vercel.json << EOF
{
  "version": 2,
  "builds": [
    {
      "src": "**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/\$1"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        }
      ]
    }
  ]
}
EOF
    
    echo -e "${GREEN}✅ Created vercel.json configuration${NC}"
    echo -e "${YELLOW}📋 Manual steps:${NC}"
    echo -e "   1. Install Vercel CLI: npm i -g vercel"
    echo -e "   2. Run: vercel --prod"
    echo -e "   3. Follow the prompts to deploy"
}

# Function to test locally
test_local() {
    echo -e "${YELLOW}🧪 Starting local development server...${NC}"
    
    if command_exists python3; then
        echo -e "${GREEN}✅ Using Python 3${NC}"
        python3 serve.py
    elif command_exists python; then
        echo -e "${GREEN}✅ Using Python${NC}"
        python serve.py
    else
        echo -e "${RED}❌ Python is not installed${NC}"
        echo -e "${YELLOW}💡 Alternative: Open index.html directly in your browser${NC}"
        open index.html 2>/dev/null || echo "Please open index.html in your browser"
    fi
}

# Function to show deployment status
show_status() {
    echo -e "${BLUE}📊 Deployment Status${NC}"
    echo -e "${BLUE}==================${NC}"
    
    # Check Git status
    if [ -d .git ]; then
        echo -e "${GREEN}✅ Git repository initialized${NC}"
        if git remote get-url origin >/dev/null 2>&1; then
            echo -e "${GREEN}✅ GitHub remote configured${NC}"
        else
            echo -e "${YELLOW}⚠️  GitHub remote not configured${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Not a Git repository${NC}"
    fi
    
    # Check files
    if [ -f "index.html" ]; then
        echo -e "${GREEN}✅ Website files present${NC}"
    else
        echo -e "${RED}❌ Website files missing${NC}"
    fi
    
    # Check configuration files
    if [ -f "netlify.toml" ]; then
        echo -e "${GREEN}✅ Netlify configuration ready${NC}"
    fi
    
    if [ -f "vercel.json" ]; then
        echo -e "${GREEN}✅ Vercel configuration ready${NC}"
    fi
}

# Main menu
echo ""
echo -e "${BLUE}Select deployment option:${NC}"
echo -e "${YELLOW}1)${NC} GitHub Pages"
echo -e "${YELLOW}2)${NC} Netlify"
echo -e "${YELLOW}3)${NC} Vercel"
echo -e "${YELLOW}4)${NC} Test locally"
echo -e "${YELLOW}5)${NC} Show status"
echo -e "${YELLOW}6)${NC} Exit"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        deploy_github
        ;;
    2)
        deploy_netlify
        ;;
    3)
        deploy_vercel
        ;;
    4)
        test_local
        ;;
    5)
        show_status
        ;;
    6)
        echo -e "${GREEN}👋 Goodbye!${NC}"
        exit 0
        ;;
    *)
        echo -e "${RED}❌ Invalid option${NC}"
        exit 1
        ;;
esac
