# Google Maps API Setup Guide

## IMPORTANT: Secure Your API Key Before Public Sharing

Your current API key is embedded in the HTML files. Follow these steps to secure it:

## Step 1: Set Up Google Cloud Console

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Navigate to**: APIs & Services > Credentials
3. **Find your API key**: `AIzaSyBH_yuU7_TfAJmu...`

## Step 2: Add Domain Restrictions (CRITICAL)

**Click "Edit" on your API key**, then:

1. Under "Application restrictions", select **"HTTP referrers"**
2. Add your GitHub Pages domain:
   ```
   https://YOUR_USERNAME.github.io/dbs-dashboard/*
   ```
3. Also add localhost for testing:
   ```
   http://localhost/*
   http://127.0.0.1/*
   ```
4. Click **"Save"**

## Step 3: Set API Usage Quotas (Cost Control)

1. Go to **APIs & Services > Dashboard**
2. Click **"Maps JavaScript API"**
3. Click **"Quotas"**
4. Set daily limits:
   - **Map loads per day**: 25,000 (covers ~800 visitors/day)
   - **Cost cap**: Set budget alert at $5/month

## Step 4: Enable Budget Alerts

1. Go to **Billing > Budgets & alerts**
2. Create budget:
   - Name: "DBS Dashboard"
   - Budget: $10/month
   - Alert threshold: 50%, 90%, 100%

## Expected Costs

With domain restrictions:
- **0-100 visitors/day**: $0 (free tier covers)
- **100-1000 visitors/day**: $0-5/month
- **>1000 visitors/day**: Contact for institutional hosting

## Security Checklist

- [ ] Domain restrictions added
- [ ] API quotas configured
- [ ] Budget alerts enabled
- [ ] Tested from GitHub Pages URL
- [ ] Removed API key from any public repositories

## Testing Your Restrictions

After adding restrictions:
1. Open your GitHub Pages URL
2. Verify maps load correctly
3. Try opening same page from different domain (should fail)

## Troubleshooting

**Maps don't load after restrictions**: Wait 5 minutes for restrictions to propagate

**"This API key is not authorized"**: Check domain spelling in restrictions

**Still seeing charges**: Verify quotas are active and check Usage report
