# DEPLOYMENT INSTRUCTIONS - DBS Dashboard to GitHub Pages

## Current Status: Ready to Deploy ✅

Your dashboard is fully prepared and committed to git locally. You just need to create the GitHub repository and push.

---

## Step 1: Create GitHub Repository (2 minutes)

1. Go to: **https://github.com/new**

2. Fill in repository details:
   - **Repository name**: `dbs-dashboard`
   - **Description**: `DBS Access Disparities Dashboard - Interactive Maps for Canada`
   - **Visibility**: Select **Public** (required for free GitHub Pages)
   - **IMPORTANT**: Do NOT check any boxes:
     - ❌ Do NOT add README
     - ❌ Do NOT add .gitignore
     - ❌ Do NOT add license

3. Click **"Create repository"**

---

## Step 2: Push Your Code (30 seconds)

Once the repository is created, run this command in your terminal:

```bash
cd /Users/ramihatoum/Desktop/PPA/maps/public_dashboard
git push -u origin main
```

Expected output:
```
Enumerating objects: ...
Counting objects: 100% ...
Writing objects: 100% ...
To https://github.com/ramihatou97/dbs-dashboard.git
 * [new branch]      main -> main
```

---

## Step 3: Enable GitHub Pages (1 minute)

1. Go to your repository: `https://github.com/ramihatou97/dbs-dashboard`

2. Click **Settings** (top right)

3. In left sidebar, click **Pages**

4. Under "Source":
   - Branch: Select **main**
   - Folder: Select **/ (root)**
   - Click **Save**

5. Wait 2-3 minutes for deployment

6. Your dashboard will be live at:
   ```
   https://ramihatou97.github.io/dbs-dashboard/
   ```

---

## Step 4: Secure Your API Key (5 minutes) - CRITICAL! 🔒

**DO THIS BEFORE SHARING THE URL**

Follow the instructions in `API_SETUP_GUIDE.md`:

1. Go to: https://console.cloud.google.com/apis/credentials

2. Find your API key and click Edit

3. Under "Application restrictions":
   - Select **HTTP referrers (web sites)**
   - Click **Add an item**
   - Add: `https://ramihatou97.github.io/dbs-dashboard/*`
   - Add: `http://localhost/*` (for local testing)
   - Click **Save**

4. Set up budget alerts:
   - Go to: https://console.cloud.google.com/billing/budgets
   - Create budget: $10/month
   - Set alerts at 50%, 90%, 100%

---

## Troubleshooting

### "Repository not found" error
- Make sure you created the repository at https://github.com/new
- Repository must be named exactly: `dbs-dashboard`
- Repository must be owned by: `ramihatou97`

### Maps don't load after deployment
- Wait 5 minutes after adding API restrictions (takes time to propagate)
- Check browser console for errors
- Verify API key restrictions include your GitHub Pages URL

### "This page can't be found" error
- Wait 2-3 minutes after enabling GitHub Pages
- Check Settings > Pages shows: "Your site is live at..."
- Try hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

---

## Quick Reference URLs

- **Create Repository**: https://github.com/new
- **Your Repository** (after creation): https://github.com/ramihatou97/dbs-dashboard
- **Your Dashboard** (after deployment): https://ramihatou97.github.io/dbs-dashboard/
- **Google Cloud Console**: https://console.cloud.google.com/
- **API Credentials**: https://console.cloud.google.com/apis/credentials

---

## What's Already Done ✅

- ✅ Dashboard package created (720 KB)
- ✅ All 6 map files included
- ✅ Index.html with tabbed navigation
- ✅ Documentation (README.md, API_SETUP_GUIDE.md)
- ✅ .gitignore configured
- ✅ Git repository initialized
- ✅ All files committed to git
- ✅ Remote repository configured

**You only need to**:
1. Create the GitHub repository online
2. Run `git push -u origin main`
3. Enable GitHub Pages in Settings
4. Secure your API key

---

## Cost Expectations

With proper API restrictions:
- **Free tier**: ~25,000 map loads/month
- **Typical cost**: $0-5/month for academic traffic
- **Budget alert**: Set at $10/month for safety

---

## Need Help?

- GitHub Pages Docs: https://docs.github.com/en/pages
- Google Maps API Docs: https://developers.google.com/maps
- README.md: Full documentation in this folder
- API_SETUP_GUIDE.md: Detailed API security instructions

---

**Generated**: November 2, 2025
**Status**: READY FOR DEPLOYMENT
