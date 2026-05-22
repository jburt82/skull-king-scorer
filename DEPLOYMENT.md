# Skull King Scorer - Deployment Guide

## Step 1: Generate App Icons

You need PNG icons at these sizes: 72x72, 96x96, 128x128, 144x144, 152x152, 192x192, 384x384, 512x512

### Option A: Use an Online Tool (Easiest)

1. Go to https://www.favicon-generator.org/ or https://www.img2go.com/resize-image
2. Upload a skull icon image (or create one)
3. Download/export as PNG at each required size
4. Create an `icons` folder in your project root
5. Place the 8 PNG files in the `icons` folder

### Option B: Use ImageMagick (Command Line)

If you have ImageMagick installed:

```bash
# Create icons folder
mkdir icons

# If you have a source image (e.g., skull.png):
convert skull.png -resize 72x72 icons/icon-72x72.png
convert skull.png -resize 96x96 icons/icon-96x96.png
convert skull.png -resize 128x128 icons/icon-128x128.png
convert skull.png -resize 144x144 icons/icon-144x144.png
convert skull.png -resize 152x152 icons/icon-152x152.png
convert skull.png -resize 192x192 icons/icon-192x192.png
convert skull.png -resize 384x384 icons/icon-384x384.png
convert skull.png -resize 512x512 icons/icon-512x512.png
```

### Option C: Use Python Script

Create `generate_icons.py` in your project folder:

```python
from PIL import Image, ImageDraw, ImageFont
import os

# Create icons directory
os.makedirs('icons', exist_ok=True)

# Create a simple skull icon using PIL
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    # Create image with gold background
    img = Image.new('RGB', (size, size), color='#0a1628')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple skull shape using circles
    # You can customize this design
    center_x, center_y = size // 2, size // 2
    skull_size = int(size * 0.7)
    
    # Main skull
    draw.ellipse(
        [center_x - skull_size//2, center_y - skull_size//3, 
         center_x + skull_size//2, center_y + skull_size//2],
        fill='#c9a227'
    )
    
    # Eyes
    eye_offset = int(skull_size * 0.15)
    eye_size = int(skull_size * 0.15)
    draw.ellipse([center_x - eye_offset - eye_size//2, center_y - skull_size//4 - eye_size//2,
                  center_x - eye_offset + eye_size//2, center_y - skull_size//4 + eye_size//2],
                 fill='#0a1628')
    draw.ellipse([center_x + eye_offset - eye_size//2, center_y - skull_size//4 - eye_size//2,
                  center_x + eye_offset + eye_size//2, center_y - skull_size//4 + eye_size//2],
                 fill='#0a1628')
    
    img.save(f'icons/icon-{size}x{size}.png')
    print(f'Created icon-{size}x{size}.png')

print('All icons generated successfully!')
```

Run it with: `python generate_icons.py`

---

## Step 2: Deploy to a Web Server

### Option A: Netlify (Recommended - Easiest)

1. Go to https://netlify.com and sign up
2. Click "Add new site" → "Deploy manually"
3. Drag and drop your project folder (skull-king-scorer)
4. Your app is now live with HTTPS automatically!
5. Get your live URL (e.g., https://skull-king-scorer.netlify.app)

**Pros:** Free, automatic HTTPS, simple drag-and-drop deployment

### Option B: Vercel

1. Go to https://vercel.com and sign up
2. Click "New Project" → "Import Git Repository"
3. Or upload your folder directly
4. Your app deploys automatically with HTTPS
5. Get your live URL

**Pros:** Fast, free, automatic HTTPS, great performance

### Option C: GitHub Pages (Free)

1. Create a GitHub account if you don't have one
2. Create a new repository named `skull-king-scorer`
3. Push your project files to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/skull-king-scorer.git
   git push -u origin main
   ```
4. Go to repository Settings → Pages
5. Select "Deploy from a branch" → select `main` branch
6. Your app is live at `https://YOUR_USERNAME.github.io/skull-king-scorer`

**Note:** Update manifest.json `start_url` to `./` or `./skull-king-scorer/` depending on deployment

### Option D: Self-Hosted (Your Own Server)

1. Upload all files to your web server
2. Make sure HTTPS is enabled (use Let's Encrypt for free SSL)
3. The app will be at your domain

---

## Step 3: Test Installation on Phone

### Android:
1. Open the deployed URL in Chrome
2. Tap the menu (⋮) → "Install app" or look for install prompt
3. The app installs to your home screen

### iOS (Limited Support):
1. Open the deployed URL in Safari
2. Tap Share → "Add to Home Screen"
3. Note: iOS doesn't fully support PWA features like offline mode

---

## After Deployment

### Monitor Data
- Game data is stored locally in the browser (localStorage)
- Users can export data by accessing browser console (advanced users)
- Consider adding an export/backup feature

### Update Your App
1. Update files locally
2. Re-deploy using your hosting service
3. Service worker will cache new version automatically

### Share Your App
- Share the live URL with friends/players
- They can install it as a phone app from the URL

---

## Quick Checklist

- [ ] Generate 8 icon PNG files
- [ ] Place icons in `icons/` folder
- [ ] Choose hosting platform (Netlify, Vercel, or GitHub Pages)
- [ ] Deploy your project
- [ ] Test installation on Android phone
- [ ] Share the URL!

