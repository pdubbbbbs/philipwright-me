# Adding Videos to Your Website

## 📹 Where to Find Your Original Videos

### 1. **Check Your Device Storage**
Search your computer for video files:
```bash
# macOS/Linux
find ~ -name "*.mp4" -o -name "*.mov" -o -name "*.webm" -o -name "*.avi" 2>/dev/null

# Or use Spotlight on macOS
# Press Cmd+Space and search for: kind:movie
```

### 2. **Cloud Storage**
Check these locations:
- **iCloud Photos** (check "All Photos" and "Videos")
- **Google Drive** 
- **Dropbox**
- **OneDrive**
- **Google Photos**

### 3. **Social Media Platforms**
Your videos might be on:
- **LinkedIn** (if you shared work demos)
- **YouTube** (private/unlisted videos)
- **Vimeo**
- **Twitter/X**

### 4. **Email Archives**
Search your email for:
- Attachments with video extensions
- Links to video hosting services
- Emails to/from clients with "video" or "demo"

### 5. **External Drives & Backups**
- Time Machine backups
- External hard drives
- USB drives
- Old computers

## 🔧 How to Add Videos to Your Website

### Method 1: Direct Video Files
1. **Place videos in the `videos/` folder**
2. **Update the HTML** in `index.html`:

```html
<!-- Replace the video placeholder section with: -->
<div class="video-container">
    <video controls poster="assets/images/video-thumbnail.jpg">
        <source src="videos/your-video.mp4" type="video/mp4">
        <source src="videos/your-video.webm" type="video/webm">
        Your browser does not support the video tag.
    </video>
</div>
```

### Method 2: YouTube/Vimeo Embed
If your videos are on YouTube or Vimeo:

```html
<!-- YouTube -->
<div class="video-container">
    <iframe src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
            frameborder="0" 
            allowfullscreen></iframe>
</div>

<!-- Vimeo -->
<div class="video-container">
    <iframe src="https://player.vimeo.com/video/YOUR_VIDEO_ID" 
            frameborder="0" 
            allowfullscreen></iframe>
</div>
```

## 📁 Recommended File Structure

```
philipwright-me/
├── videos/
│   ├── project-demo-1.mp4
│   ├── project-demo-2.mp4
│   └── portfolio-showcase.mov
├── assets/
│   └── images/
│       ├── video-thumbnail-1.jpg
│       └── video-thumbnail-2.jpg
└── index.html
```

## ✨ Best Practices for Web Videos

### 1. **File Formats**
- **MP4**: Best compatibility (use H.264 codec)
- **WebM**: Better compression, modern browsers
- **MOV**: Keep as backup, convert for web

### 2. **File Size Optimization**
```bash
# Using FFmpeg to optimize videos:
ffmpeg -i input.mov -c:v libx264 -crf 23 -c:a aac -b:a 128k output.mp4
```

### 3. **Create Thumbnails**
```bash
# Generate thumbnail at 5 seconds
ffmpeg -i input.mp4 -ss 5 -vframes 1 thumbnail.jpg
```

### 4. **Multiple Quality Options**
Consider offering different quality options:
- 1080p for desktop
- 720p for tablets
- 480p for mobile

## 🎬 Video Content Ideas

Based on pw8away.com style, consider showcasing:

1. **Project Walkthroughs**
   - Screen recordings of applications
   - Live demonstrations
   - Before/after comparisons

2. **Process Videos**
   - Design process timelapse
   - Development workflow
   - Problem-solving approach

3. **Client Testimonials**
   - Short testimonial videos
   - Case study presentations

## 🔍 Search Strategies for Lost Videos

### Wayback Machine URLs to Check:
- https://web.archive.org/web/*/philipwright.me/*
- Check specific dates when you remember having videos

### Google Search:
```
site:philipwright.me filetype:mp4
site:philipwright.me "video"
"Philip Wright" video demo
```

### Social Media Search:
- Search your own posts for video content
- Check saved items/bookmarks
- Look through old stories/highlights

## 📞 Need Help?

If you find video files but need help:
1. **Converting formats**: Use HandBrake (free) or FFmpeg
2. **Compressing large files**: Use online tools or FFmpeg
3. **Creating thumbnails**: Use video editing software or FFmpeg

## 🚀 Quick Start When You Find Videos

1. **Copy videos** to the `videos/` folder
2. **Create thumbnails** and put them in `assets/images/`
3. **Update the HTML** in the video placeholder sections
4. **Test locally** by opening `index.html` in your browser
5. **Commit and push** to GitHub when ready

Remember: The website is already set up with video-ready styling and structure. You just need to drop in your content and update the HTML paths!
