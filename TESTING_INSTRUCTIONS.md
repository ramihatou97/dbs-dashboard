# DBS Access Dashboard - Testing Instructions

## 🧪 How to Verify the Fix

### Quick Test (2 minutes)

**Step 1**: Open the main map
```
File: /Users/ramihatoum/Desktop/PPA/maps/public_dashboard/map1_travel_burden_heatmap.html
Action: Double-click or right-click → Open With → Chrome/Firefox/Safari
```

**Step 2**: Check that the map loads
- ✅ Expected: Google Maps displays with colored markers
- ✗ Error: "This page didn't load Google Maps correctly"
  - If you see this, check Google Cloud Console (see troubleshooting below)

**Step 3**: Verify specific FSAs

### Saskatchewan FSAs (Previously Problematic)

**FSA S0K** (Excellent Access - Green):
- Distance: 32.7 km
- Expected: Marker appears CLOSE to Royal University Hospital, Saskatoon
- Color: Green (Excellent 0-50km category)
- Location: Should be near Saskatoon city center

**FSA S0E** (Poor Access - Orange):
- Distance: 256.5 km
- Expected: Marker appears FAR from any hospital
- Color: Orange (Poor 200-400km category)
- Location: Northeast Saskatchewan, remote area

**FSA S0L** (Moderate Access - Yellow):
- Distance: 158.8 km
- Expected: Marker at moderate distance from Royal University Hospital
- Color: Yellow (Moderate 100-200km category)
- Location: West-central Saskatchewan

**FSA S0A** (Poor Access - Orange):
- Distance: 295.9 km
- Expected: Marker FAR from hospitals
- Color: Orange (Poor 200-400km category)
- Location: Southeast Saskatchewan

---

## 📋 Comprehensive Testing Checklist

### Test All 7 Maps:

1. ☐ **map1_travel_burden_heatmap.html**
   - Verify color coding matches visual distance
   - Check legend displays correctly
   - Test distance filter dropdown

2. ☐ **map2_vulnerability_index.html**
   - Verify vulnerability scores align with marker colors
   - Check socioeconomic overlays

3. ☐ **map3_indigenous_access_crisis.html**
   - Verify indigenous FSAs are highlighted correctly
   - Check crisis designation for remote areas

4. ☐ **map4_service_gaps_multibarrier.html**
   - Verify multi-barrier FSAs show correct overlapping factors
   - Check barrier count labels

5. ☐ **map5_patient_flow_lines.html**
   - Verify flow lines connect FSAs to nearest hospital
   - Check line colors represent distance categories

6. ☐ **distance_map.html**
   - Basic distance visualization
   - Test heatmap toggle

7. ☐ **combined_analysis.html**
   - Test layer switching (distance, income, indigenous, etc.)
   - Verify sidebar updates on marker click

---

## 🔍 What to Look For

### ✅ Correct Behavior:
1. **Visual-Distance Alignment**
   - Green markers (0-50km) appear close to hospitals
   - Red markers (400+km) appear very far from hospitals
   - Orange/yellow markers at intermediate distances

2. **Marker Placement Logic**
   - Markers placed at population centroids (not random locations)
   - Urban FSAs cluster around city centers
   - Remote FSAs scattered in northern/rural areas

3. **Interactive Features**
   - Click markers → Info popup shows FSA details
   - Filters work correctly
   - Legend matches marker colors

### ✗ Incorrect Behavior (Report These):
1. **Visual Mismatches**
   - Green marker (excellent access) far from hospital
   - Red marker (poor access) close to hospital
   - Distance value doesn't match visual placement

2. **Loading Errors**
   - "This page didn't load Google Maps correctly"
   - Gray box instead of map
   - JavaScript console errors

3. **Data Errors**
   - Missing markers
   - Incorrect FSA labels
   - Wrong distance values

---

## 🐛 Troubleshooting

### Error: "This page didn't load Google Maps correctly"

**Cause**: Google Cloud Console configuration issue

**Solutions** (try in order):

1. **Enable Maps JavaScript API**
   ```
   1. Go to: https://console.cloud.google.com/apis/library
   2. Search: "Maps JavaScript API"
   3. Click it → Click "ENABLE"
   4. Wait 2-3 minutes → Refresh browser
   ```

2. **Enable Billing**
   ```
   1. Go to: https://console.cloud.google.com/billing
   2. Link a billing account (free tier: $200/month credit)
   3. Wait 5 minutes → Refresh browser
   ```

3. **Check API Key Restrictions**
   ```
   1. Go to: https://console.cloud.google.com/apis/credentials
   2. Click your API key: AIzaSyBH_yuU7_TfAJmuf_h04UsmKKhC0XPWerA
   3. Under "Application restrictions":
      - Temporarily set to "None" for testing
      - OR add these referrers:
        * http://localhost/*
        * http://127.0.0.1/*
        * file:///*
   4. Click "Save" → Wait 5 minutes → Refresh browser
   ```

4. **Check Browser Console**
   ```
   - Open Developer Tools (F12 or Cmd+Option+I)
   - Click "Console" tab
   - Look for red error messages
   - Copy error text and search Google for solution
   ```

---

## ✅ Expected Test Results

### All FSAs Verified:
```
✓ S0K: 32.7 km   → Green marker near Saskatoon
✓ S0E: 256.5 km  → Orange marker in remote area
✓ S0L: 158.8 km  → Yellow marker at moderate distance
✓ S0A: 295.9 km  → Orange marker far from hospitals
✓ X0X: 4739.5 km → Red marker in Arctic (Nunavut)
✓ X0A: 3781.5 km → Red marker in Arctic (Nunavut)
✓ M0E: 29.1 km   → Green marker near Toronto
✓ M3T: 10.5 km   → Green marker in Toronto core
✓ L7W: 465.9 km  → Red marker (assigned to Ottawa, far)
✓ S0P: 152.7 km  → Yellow marker in remote Saskatchewan
```

### Coordinate Sources:
```
✓ 507 FSAs (99.2%) → Statistics Canada population centroids
✓ 4 FSAs (0.8%)    → Manual overrides (L7W, M0E, M3T, X0X)
✓ 0 FSAs (0%)      → Google Geocoding (not needed)
✓ 0 FSAs (0%)      → Approximation (not needed)
```

---

## 📊 Success Criteria

### ✅ Fix is Successful If:
1. All 7 maps load without errors
2. Green markers appear close to hospitals
3. Red markers appear far from hospitals
4. Clicking markers shows accurate FSA info
5. Distance values match visual placement
6. No "didn't load correctly" errors

### ✗ Fix Failed If:
1. Maps don't load (Google API error)
2. Visual distance doesn't match color coding
3. Markers placed at wrong coordinates
4. FSA data missing or incorrect

---

## 📝 Testing Report Template

After testing, report results:

```
Date Tested: _______________
Browser: _______________
OS: _______________

MAP LOADING:
☐ All maps load correctly
☐ Some maps have errors (list which ones):
   _________________________________

FSA VERIFICATION:
☐ S0K appears close to Saskatoon (green)
☐ S0E appears far from hospitals (orange)
☐ S0L at moderate distance (yellow)
☐ S0A far from hospitals (orange)

ISSUES FOUND:
_________________________________
_________________________________

OVERALL STATUS:
☐ Fix successful - all tests passed
☐ Fix incomplete - issues remain
☐ Fix failed - major problems
```

---

## 🎯 Next Steps After Testing

**If All Tests Pass:**
- ✅ Data integrity restored
- ✅ Maps ready for research/publication
- ✅ Document any specific findings

**If Tests Fail:**
- Check troubleshooting section above
- Review browser console for errors
- Verify Google Cloud Console settings
- Contact developer with specific error messages

---

**Last Updated**: November 2, 2025
**Fix Version**: v2.0 - Population Centroid Alignment
**Testing Duration**: ~10 minutes for full verification
