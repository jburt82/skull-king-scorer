# Quick Start: Deploy Skull King Scorer to the Web

## 5-Minute Deployment Guide

### Step 1: Generate Icons (2 minutes)

**Option A: Using Python (Easiest)**
```bash
# Install Pillow if needed:
pip install Pillow

# Run the icon generator:
python generate_icons.py
```

**Option B: Using Online Tool**
- Go to https://www.favicon-generator.org/
- Upload or create a skull icon
- Download at sizes: 72, 96, 128, 144, 152, 192, 384, 512
- Create `icons` folder and place PNG files inside

### Step 2: Deploy to Netlify (3 minutes)

1. **Sign up for Netlify** (free)
   - Go to https://netlify.com
   - Click "Sign up" → use GitHub/Google account or email

2. **Deploy your app**
   - Drag and drop your `skull-king-scorer` folder onto Netlify
   - Or click "New site" → "Deploy manually" → drag and drop

3. **Done!**
   - Netlify automatically assigns you a live URL
   - Your app is now on the web with HTTPS!
   - Share the URL with friends

---

## Test on Your Phone

### Android:
1. Open your Netlify URL in Chrome on your phone
2. Look for the "Install" prompt (or tap menu ⋮ → "Install app")
3. Tap "Install" - it's now on your home screen!

### iPhone:
1. Open your Netlify URL in Safari
2. Tap Share button → "Add to Home Screen"
3. The app appears on your home screen

---

## What You Get

✅ **Live game scorer app**  
✅ **Works offline** (thanks to service worker)  
✅ **Installs as a phone app**  
✅ **Free HTTPS** (secure)  
✅ **No server fees**  

---

## Future Updates

When you update your app:
1. Update files locally
2. Re-deploy to Netlify (drag and drop again or connect GitHub)
3. The app automatically updates on users' phones

---

## Alternative Deployment Options

| Service | Cost | Ease | Setup Time |
|---------|------|------|-----------|
| **Netlify** | Free | Easiest | 2 min |
| **Vercel** | Free | Very Easy | 3 min |
| **GitHub Pages** | Free | Easy | 5 min |
| **Self-hosted** | Varies | Harder | 30+ min |

---

## Troubleshooting

**"My icons aren't showing"**
- Make sure the `icons` folder is in the project root directory
- Verify the PNG files exist at the correct sizes

**"Install button doesn't appear"**
- Verify the app is served over HTTPS (Netlify does this automatically)
- Wait a few seconds - the prompt appears after page load
- Try reloading the page

**"It says 'No previous games yet' on first launch"**
- This is correct! Game history only appears after you play your first game

---

## Support

For detailed instructions, see `DEPLOYMENT.md`

For Netlify help: https://docs.netlify.com/

Questions? Check the troubleshooting in DEPLOYMENT.md
