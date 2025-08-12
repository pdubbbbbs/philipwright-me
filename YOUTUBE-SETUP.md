# Adding Your YouTube Videos

## 🎬 **IMMEDIATE ACTION NEEDED**

Your website is **ready to go** but needs your YouTube video IDs! Here's exactly what to do:

## 🔍 **Step 1: Find Your YouTube Videos**

### Option A: Go to Your YouTube Channel
1. Visit `https://youtube.com/@pdubbbbbs` or search "pdubbbbbs" on YouTube
2. Find the videos you want to showcase
3. Copy the URLs of your best videos

### Option B: Search YouTube for Your Content
1. Go to YouTube.com
2. Search: `"Philip Wright" programming` or `"Philip Wright" tech` or `pdubbbbbs`
3. Find your videos and copy the URLs

### Option C: Check Your YouTube Studio
1. Go to `https://studio.youtube.com`
2. Sign in with your Google account
3. View your uploaded videos
4. Copy the URLs of videos you want to feature

## ⚡ **Step 2: Extract Video IDs**
From any YouTube URL like: `https://www.youtube.com/watch?v=ABC123xyz`
The video ID is: **ABC123xyz** (the part after `v=`)

## 🛠️ **Step 3: Update Your Website**

Open `index.html` and replace these **4 placeholders**:

```html
<!-- MAIN FEATURED VIDEO (Large) -->
Replace: dQw4w9WgXcQ
With: YOUR_MAIN_VIDEO_ID

<!-- WORK SECTION VIDEOS (Smaller) -->
Replace: YOUR_VIDEO_ID_2
With: YOUR_SECOND_VIDEO_ID

Replace: YOUR_VIDEO_ID_3  
With: YOUR_THIRD_VIDEO_ID

Replace: YOUR_VIDEO_ID_4
With: YOUR_FOURTH_VIDEO_ID
```

## 🔍 Possible Video IDs I Found:
Based on searches for "Philip Wright" and "pdubbbbbs":
- `KTX8uaf-lus`
- `_zdv23bAINM`
- `JbdbboQ4RCs`
- `ofiSYwNk8l8`
- `LmE9EQE_IgM`

**Check these on YouTube to see if any are yours!**

## 📋 Example Usage:
If your video ID is `ABC123xyz`, change this:
```html
src="https://www.youtube.com/embed/YOUR_VIDEO_ID?rel=0&showinfo=0&modestbranding=1"
```

To this:
```html
src="https://www.youtube.com/embed/ABC123xyz?rel=0&showinfo=0&modestbranding=1"
```

## 🚀 Test Your Changes:
1. Save the file
2. Open `index.html` in your browser
3. Your videos should load!

## 💡 Pro Tips:
- Use your best/most professional video for the main featured section
- Choose shorter videos for the work cards section
- Make sure your videos are public or unlisted (not private)
