# DBS Access Dashboard - Comprehensive Summary

**Last Updated**: November 2, 2025
**Version**: 2.1 (Unified Dashboard)
**Status**: Production Ready

---

## Overview

The **DBS Access Disparities Dashboard** is a comprehensive interactive platform providing 9 distinct visualizations analyzing Deep Brain Stimulation (DBS) surgery access across Canada. The dashboard combines geographic, socioeconomic, and demographic data to reveal disparities in healthcare access.

**Dashboard URL**: `/Users/ramihatoum/Desktop/PPA/maps/public_dashboard/index.html`

---

## Dashboard Structure

### Architecture: Tab-Based Interface with Iframes

The dashboard uses a modern tab-based navigation system where each visualization is loaded via iframe. This approach provides:
- **Fast initial load**: Only the active tab's content loads initially
- **Modular design**: Each visualization is independent
- **Easy maintenance**: Update individual maps without affecting others
- **Responsive layout**: Adapts to desktop, tablet, and mobile screens

### Navigation System

```
Tab 1: Travel Burden → map1_travel_burden_heatmap.html (112K)
Tab 2: Vulnerability Index → map2_vulnerability_index.html (122K)
Tab 3: Indigenous Access → map3_indigenous_access_crisis.html (138K)
Tab 4: Service Gaps → map4_service_gaps_multibarrier.html (127K)
Tab 5: Patient Flows → map5_patient_flow_lines.html (106K)
Tab 6: Distance Map → distance_map.html (115K)
Tab 7: Combined Analysis → combined_analysis.html (232K)
Tab 8: Regional Flows (Sankey) → archive/patient_flow_sankey.html (4.6M)
Tab 9: Provincial Comparison → archive/provincial_comparison.html (4.6M)
```

---

## The 9 Visualizations

### 1. Travel Burden Heatmap
**File**: `map1_travel_burden_heatmap.html` (112K)
**Type**: Google Maps with color-coded markers

**What It Shows**:
- All 511 FSAs color-coded by distance to nearest DBS center
- Green (0-50km): Excellent access
- Yellow (50-200km): Moderate access
- Orange (200-400km): Poor access
- Red (400+km): Very poor access

**Key Features**:
- Interactive markers with FSA details on click
- Distance-based filtering dropdown
- Legend showing category definitions
- Heatmap overlay option

**Data Fields Present**:
- FSA code
- Distance to nearest center (km)
- Nearest DBS center name
- Distance category

**Socioeconomic Fields**: ❌ None

---

### 2. Vulnerability Index
**File**: `map2_vulnerability_index.html` (122K)
**Type**: Google Maps with vulnerability scoring

**What It Shows**:
- FSAs scored by combined distance and socioeconomic factors
- Vulnerability = (Distance × 0.4) + (Socioeconomic factors × 0.6)
- Color gradient from low (green) to high (red) vulnerability

**Key Features**:
- Composite vulnerability scoring algorithm
- Accounts for employment, housing, education barriers
- Interactive vulnerability tooltips
- Filter by vulnerability level

**Data Fields Present**:
- FSA code
- Distance to nearest center
- Vulnerability score (0-100)
- Vulnerability category

**Socioeconomic Fields**: ❌ None (uses composite vulnerability score, not raw fields)

---

### 3. Indigenous Access Crisis
**File**: `map3_indigenous_access_crisis.html` (138K)
**Type**: Google Maps highlighting indigenous barriers

**What It Shows**:
- FSAs with significant Indigenous populations (>5%)
- Combined with distance barriers
- 40 FSAs identified as "crisis zones" (high Indigenous + extreme distance)

**Key Features**:
- Indigenous population percentage labels
- Crisis designation markers (red stars)
- Distance + indigenous population overlay
- Focus on northern and remote communities

**Data Fields Present**:
- FSA code
- Distance to nearest center
- Indigenous population presence indicator
- Crisis zone designation

**Socioeconomic Fields**: ❌ None (shows indigenous presence but not raw indigenous_ancestry_rate)

---

### 4. Multi-Barrier Service Gaps
**File**: `map4_service_gaps_multibarrier.html` (127K)
**Type**: Google Maps with multi-factor analysis

**What It Shows**:
- FSAs facing multiple simultaneous barriers:
  - Distance barrier (>200km)
  - Low income (<$50k median)
  - High indigenous population (>5%)
- Barrier count visualization (1, 2, or 3 barriers)

**Key Features**:
- Stacked barrier identification
- Color intensity based on barrier count
- Multi-barrier FSA clustering
- Interactive barrier breakdown on click

**Data Fields Present**:
- FSA code
- Distance barrier status
- Income barrier status
- Indigenous barrier status
- Total barrier count (1-3)

**Socioeconomic Fields**: ❌ None (uses binary indicators, not raw values)

---

### 5. Patient Flow Lines (Enhanced with Animated Arrows)
**File**: `map5_patient_flow_lines.html` (106K)
**Type**: Google Maps with enhanced animated directional flow arrows

**What It Shows**:
- Visual flow lines from all 511 FSAs to their nearest DBS center
- **Animated arrows** showing travel direction along flow paths
- **Gradient color scheme** based on distance (5 tiers)
- **Dynamic line thickness** - longer distances get thicker, more prominent lines
- Dramatic visualization emphasizing long-distance healthcare access barriers

**Key Features**:
- **Animated directional arrows** that move along flow lines
- **5-tier gradient color scheme**:
  - Green (0-50 km): Excellent access
  - Yellow-green (50-100 km): Good access
  - Yellow (100-200 km): Moderate access
  - Orange (200-500 km): Poor access
  - Red (500+ km): Very poor access
- **Dynamic styling**: Line weight and opacity increase with distance
- **Interactive hover tooltips**: Show FSA → Center and exact distance
- **Hover effects**: Lines brighten and thicken on mouseover
- **Distance color legend**: Left-side legend explaining gradient
- **Center rankings legend**: Right-side legend showing FSA counts
- **Priority rendering**: Long-distance flows rendered on top
- Shows catchment areas for each center
- Flow pattern analysis

**Visual Enhancements**:
- Arrow animation: 100ms update interval for smooth movement
- White stroke on arrows for visibility against all backgrounds
- Z-index based on distance: longer flows appear above shorter ones
- Higher opacity for long distances (0.8 vs 0.4 for short distances)
- Geodesic lines follow Earth's curvature for accuracy

**Data Fields Present**:
- FSA code
- Start coordinates (FSA centroid)
- End coordinates (DBS center)
- Distance to center (km)
- Nearest center name
- Flow direction and path

**Socioeconomic Fields**: ❌ None

**Unique Value**: Most visually dramatic representation of access disparities. Animated arrows clearly show direction and magnitude of patient travel burden. Long-distance flows (Arctic regions, remote areas) are highly emphasized through thicker lines and higher opacity.

---

### 6. Distance Map (Basic Visualization)
**File**: `distance_map.html` (115K)
**Type**: Google Maps with simplified view

**What It Shows**:
- Simplified distance visualization
- All FSAs with basic distance color coding
- Interactive heatmap toggle
- Clean, uncluttered interface

**Key Features**:
- Toggle heatmap overlay on/off
- Basic distance categories
- Minimal UI for clarity
- Quick reference map

**Data Fields Present**:
- FSA code
- Distance to nearest center
- Distance category
- Nearest center name

**Socioeconomic Fields**: ❌ None

---

### 7. Combined Analysis (Multi-Layer View) ⭐
**File**: `combined_analysis.html` (232K)
**Type**: Google Maps with layer controls

**What It Shows**:
- Comprehensive multi-layer analysis
- **ONLY map containing ALL 4 socioeconomic fields at FSA level**
- Layer controls to switch between data views:
  - Distance view
  - Income view
  - Indigenous ancestry view
  - Gini index view
  - Visible minority view
  - Vulnerability composite view

**Key Features**:
- Layer switching controls (buttons)
- Detailed sidebar with full FSA data on click
- All socioeconomic metrics displayed
- Most comprehensive data visualization

**Data Fields Present (COMPLETE SET)**:
- FSA code
- Distance to nearest center (km)
- **median_household_income_2020** ($)
- **gini_index** (0-1 scale)
- **indigenous_ancestry_rate** (%)
- **visible_minority_rate** (%)
- Nearest DBS center name
- Distance category
- Income category
- Disparity score
- Latitude/Longitude

**Socioeconomic Fields**: ✅ **ALL 4 FIELDS PRESENT**
- median_household_income_2020
- gini_index
- indigenous_ancestry_rate
- visible_minority_rate

**JavaScript Data Structure** (line 208):
```javascript
const fsaData = [
    {"FSA": "A0G",
     "distance_to_nearest_km": 2789.911,
     "median_household_income_2020": 57600.0,
     "gini_index": 0.298,
     "indigenous_ancestry_rate": 3.43678712930724,
     "visible_minority_rate": 0.480249729859527,
     "nearest_dbs_center": "Toronto Western Hospital",
     "distance_category": "Very Poor (400+km)",
     "income_category": "Medium ($50k-$75k)",
     "disparity_score": 65.63,
     "latitude": 49.21645821101191,
     "longitude": -54.439041326893786},
    // ... 510 more FSAs with complete data
]
```

---

### 8. Regional Flows (Sankey Diagram)
**File**: `archive/patient_flow_sankey.html` (4.6M)
**Type**: Plotly Sankey diagram

**What It Shows**:
- Patient flow patterns from **16 Canadian regions** to **9 DBS centers**
- Flow thickness = patient volume
- Flow color = access quality (green=excellent, yellow=moderate, orange=poor, red=very poor)
- Reveals regional healthcare patterns and center catchment areas

**Key Features**:
- Interactive Sankey flows
- Hover for flow details (source → target, volume, quality)
- Regional aggregation (not FSA-level)
- Unique visualization not available in map-based views

**Regions (16 sources)**:
- Quebec Eastern, Quebec Montreal, Quebec Western
- Alberta, British Columbia, Manitoba
- New Brunswick, Newfoundland and Labrador
- Nova Scotia, Northwest Territories, Nunavut
- Ontario Central, Ontario Eastern, Ontario Northern, Ontario Western
- Prince Edward Island, Saskatchewan

**DBS Centers (9 targets)**:
- Toronto Western Hospital
- Centre hospitalier de l'Université de Montréal (CHUM)
- London Health Sciences Centre
- Ottawa Hospital
- Vancouver General Hospital
- Foothills Medical Centre (Calgary)
- Royal University Hospital (Saskatoon)
- Health Sciences Centre (Winnipeg)
- QEII Health Sciences Centre (Halifax)

**Data Fields Present**:
- Region name (source)
- DBS center name (target)
- Patient flow volume
- Access quality category

**Socioeconomic Fields**: ❌ None (regional flows only)

**Unique Value**: Only visualization showing regional-level patient flow patterns and inter-provincial healthcare access relationships.

---

### 9. Provincial Comparison (Multi-Panel Dashboard)
**File**: `archive/provincial_comparison.html` (4.6M)
**Type**: Plotly 4-panel dashboard

**What It Shows**:
Four comparative panels analyzing all 10 Canadian provinces:

**Panel 1: Average Travel Distance by Province** (Bar chart)
- Average driving distance for each province
- Reveals provincial-level access disparities
- Highlights provinces with poor geographic access

**Panel 2: Patient Volume by Province** (Bar chart)
- Number of patients by province
- Shows population distribution needing DBS access
- Identifies high-demand regions

**Panel 3: Income vs Distance** (Scatter plot)
- Correlation between median household income and travel distance
- Each point = one FSA
- Color-coded by province
- **Contains median_household_income_2020 data**
- Reveals socioeconomic-geographic access patterns

**Panel 4: Indigenous Population vs Distance** (Scatter plot)
- Correlation between indigenous ancestry rate and travel distance
- Each point = one FSA
- Color-coded by province
- **Contains indigenous_ancestry_rate data**
- Highlights disproportionate barriers faced by indigenous communities

**Key Features**:
- Provincial-level aggregations
- Comparative analysis across Canada
- Scatter plots with FSA-level data points
- Interactive Plotly charts (zoom, pan, hover)

**Data Fields Present**:
- Province name
- Average distance to nearest center
- Patient volume/count
- **median_household_income_2020** (Panel 3 scatter plot)
- **indigenous_ancestry_rate** (Panel 4 scatter plot)
- Individual FSA data points in scatter plots

**Socioeconomic Fields**: ✅ **2 OF 4 FIELDS PRESENT**
- median_household_income_2020 (Panel 3)
- indigenous_ancestry_rate (Panel 4)
- ❌ gini_index (not shown)
- ❌ visible_minority_rate (not shown)

**Unique Value**: Only visualization providing provincial-level aggregations and comparative analysis across all 10 provinces. Reveals macro-level access patterns not visible in FSA-level maps.

---

## Socioeconomic Data Field Availability Summary

### Complete Field Availability Matrix

| Visualization | median_household_income_2020 | gini_index | indigenous_ancestry_rate | visible_minority_rate |
|--------------|------------------------------|------------|--------------------------|----------------------|
| 1. Travel Burden | ❌ | ❌ | ❌ | ❌ |
| 2. Vulnerability Index | ❌ | ❌ | ❌ | ❌ |
| 3. Indigenous Access | ❌ | ❌ | ❌ | ❌ |
| 4. Service Gaps | ❌ | ❌ | ❌ | ❌ |
| 5. Patient Flows | ❌ | ❌ | ❌ | ❌ |
| 6. Distance Map | ❌ | ❌ | ❌ | ❌ |
| **7. Combined Analysis** | **✅** | **✅** | **✅** | **✅** |
| 8. Regional Flows (Sankey) | ❌ | ❌ | ❌ | ❌ |
| 9. Provincial Comparison | **✅** | ❌ | **✅** | ❌ |

### Key Findings

**For FSA-Level Analysis with ALL 4 Fields**:
- ✅ Use **Tab 7: Combined Analysis** (combined_analysis.html)
- This is the ONLY map with complete socioeconomic data at FSA level
- Contains all 511 FSAs with full data arrays

**For Provincial-Level Analysis with 2 Fields**:
- ✅ Use **Tab 9: Provincial Comparison** (provincial_comparison.html)
- Contains median income and indigenous ancestry rate
- Provides comparative analysis across 10 provinces

**For Distance-Only Analysis**:
- ✅ Use any of Tabs 1-6 or Tab 8
- Focus on geographic access without socioeconomic overlays

---

## Dataset Details

### Geographic Coverage
- **511 FSAs** (Forward Sortation Areas) across Canada
- **10 DBS Centers** in 9 cities
- **16 Regions** for Sankey flow analysis
- **10 Provinces** for provincial comparison

### Coordinate Data Source
- **99.2%** (507 FSAs): Statistics Canada 2021 Census Population-Weighted Centroids
- **0.8%** (4 FSAs): Manual overrides (L7W, M0E, M3T, X0X)
- **0%**: Google Geocoding API (not needed)
- **0%**: Approximation algorithm (not needed)

### Distance Calculation Methodology
- **Method**: Google Distance Matrix API
- **Type**: Driving distance via optimal road routes (NOT straight-line)
- **From**: DBS hospital addresses
- **To**: FSA population-weighted centroids
- **Data Quality**: 920 verified distance records (100% integrity)

### Socioeconomic Data Source
- **Source**: Statistics Canada 2021 Census (Catalogue: 98-401-X2021013)
- **Fields Available**:
  1. **median_household_income_2020**: Median income in 2020 dollars
  2. **gini_index**: Income inequality measure (0-1 scale, higher = more inequality)
  3. **indigenous_ancestry_rate**: Percentage with indigenous ancestry
  4. **visible_minority_rate**: Percentage identifying as visible minority

### Data Quality Metrics
- ✅ **100% data integrity** (920/920 verified records)
- ✅ **No invalid/NAN FSAs**
- ✅ **99.2% authoritative coordinates**
- ✅ **All coordinates validated** within Canada bounds (41.7°N-83.1°N, -141°W--52°W)

---

## Technical Implementation

### Frontend Technologies
- **Google Maps JavaScript API**: Interactive map rendering (7 maps)
- **Plotly.js**: Sankey diagram and multi-panel charts (2 visualizations)
- **Vanilla JavaScript**: Tab switching and interactivity
- **HTML5/CSS3**: Responsive layout and styling

### Responsive Design
- **Desktop (>1200px)**: All 9 tabs in single row with horizontal scroll
- **Tablet (768px-1200px)**: Tabs wrap with smaller font
- **Mobile (<768px)**: 2-column tab layout, full wrap

### File Structure
```
public_dashboard/
├── index.html (13K)                          # Main dashboard
├── map1_travel_burden_heatmap.html (112K)
├── map2_vulnerability_index.html (122K)
├── map3_indigenous_access_crisis.html (138K)
├── map4_service_gaps_multibarrier.html (127K)
├── map5_patient_flow_lines.html (106K)
├── distance_map.html (115K)
├── combined_analysis.html (232K)             # ⭐ All 4 socioeconomic fields
├── archive/
│   ├── patient_flow_sankey.html (4.6M)
│   ├── provincial_comparison.html (4.6M)
│   └── README.md
├── COORDINATE_DATA_SOURCE.md
├── TESTING_INSTRUCTIONS.md
└── DASHBOARD_SUMMARY.md (this file)
```

---

## User Guide

### How to Use the Dashboard

1. **Open the Dashboard**
   - File: `/Users/ramihatoum/Desktop/PPA/maps/public_dashboard/index.html`
   - Double-click or right-click → Open With → Browser (Chrome/Firefox/Safari)

2. **Navigate Between Visualizations**
   - Click any of the 9 tabs at the top
   - Tab will highlight, map will load in iframe below
   - Each tab is independent

3. **Interact with Maps** (Tabs 1-7)
   - **Zoom**: Scroll wheel or pinch
   - **Pan**: Click and drag
   - **Marker Info**: Click any FSA marker for details
   - **Filters**: Use dropdowns (where available)
   - **Layers**: Switch layers in Combined Analysis (Tab 7)

4. **Interact with Sankey Diagram** (Tab 8)
   - **Hover**: Over flows to see source → target details
   - **Zoom**: Scroll to zoom in/out
   - **Pan**: Click and drag to reposition

5. **Interact with Provincial Charts** (Tab 9)
   - **Hover**: Over bars/points for exact values
   - **Zoom**: Click and drag to zoom into regions
   - **Pan**: Shift + drag to move view
   - **Reset**: Double-click to reset zoom

### Which Tab Should I Use?

**For Overall Access Patterns**:
- → Tab 1: Travel Burden (simple distance visualization)
- → Tab 5: Patient Flows (shows travel direction arrows)

**For Socioeconomic Analysis**:
- → **Tab 7: Combined Analysis** (complete FSA-level data with all 4 fields)
- → Tab 9: Provincial Comparison (provincial aggregations with 2 fields)

**For Vulnerability Assessment**:
- → Tab 2: Vulnerability Index (composite scoring)
- → Tab 4: Multi-Barrier Service Gaps (overlapping barriers)

**For Indigenous Communities**:
- → Tab 3: Indigenous Access Crisis (highlights indigenous barriers)
- → Tab 9: Provincial Comparison (Panel 4 shows indigenous vs distance)

**For Regional Healthcare Flows**:
- → Tab 8: Regional Flows (Sankey diagram of regional patterns)

**For Provincial Comparisons**:
- → Tab 9: Provincial Comparison (4-panel provincial dashboard)

---

## Research Applications

### Suitable for:

1. **Healthcare Access Research**
   - Geographic barriers to specialized care
   - Regional disparities in DBS access
   - Travel burden quantification

2. **Health Equity Studies**
   - Socioeconomic determinants of access
   - Indigenous health disparities
   - Income-based healthcare barriers

3. **Policy Analysis**
   - DBS center placement optimization
   - Resource allocation recommendations
   - Healthcare infrastructure planning

4. **Health Geography**
   - Spatial analysis of healthcare access
   - Distance-based access modeling
   - Catchment area analysis

5. **Data Visualization Research**
   - Multi-modal healthcare data visualization
   - Interactive dashboard design
   - Geographic information systems (GIS)

---

## Maintenance and Updates

### When to Update

1. **Census Data (Every 5 Years)**
   - Download new FSA population centroids from Statistics Canada
   - Replace `fsa_population_centroids.csv`
   - Regenerate all maps

2. **Distance Recalculation**
   - If DBS hospital locations change
   - If new FSAs are created
   - Re-run Google Distance Matrix API
   - Update Excel file
   - Regenerate maps

3. **New Visualizations**
   - Add new HTML file to public_dashboard/
   - Add new tab to index.html navigation
   - Update footer count and descriptions

### How to Regenerate Maps

```bash
cd /Users/ramihatoum/Desktop/PPA/maps

# Generate specialized maps (1-5)
python3 specialized_maps_generator.py

# Generate distance & combined maps (6-7)
python3 google_maps_enhanced.py

# Fix Google Maps callback (all maps)
cd public_dashboard
python3 fix_google_maps.py

# Verify all maps load correctly
open index.html
```

---

## Troubleshooting

### Maps Don't Load

**Error**: "This page didn't load Google Maps correctly"

**Solutions**:
1. Enable Maps JavaScript API in Google Cloud Console
2. Enable Billing (free tier: $200/month credit)
3. Check API key restrictions (allow localhost/file://)
4. See `TESTING_INSTRUCTIONS.md` for detailed steps

### Archived Files Don't Load (Tabs 8-9)

**Problem**: Sankey or Provincial tabs show blank

**Check**:
1. Files exist: `archive/patient_flow_sankey.html` and `archive/provincial_comparison.html`
2. File sizes: Both should be ~4.6M
3. Browser console: Check for loading errors (F12 → Console)

### Tab Switching Doesn't Work

**Problem**: Clicking tabs doesn't change views

**Check**:
1. JavaScript enabled in browser
2. No console errors (F12 → Console)
3. `showMap()` function defined in index.html (line 292)

---

## Version History

### Version 2.1 (November 2, 2025) - Current
- ✅ Unified dashboard with 9 visualizations
- ✅ Added tabs for Sankey and Provincial visualizations
- ✅ Enhanced responsive CSS for 9-tab layout
- ✅ Updated descriptions highlighting socioeconomic data
- ✅ Comprehensive documentation created

### Version 2.0 (November 2, 2025)
- ✅ Fixed coordinate alignment using Statistics Canada centroids
- ✅ Regenerated all 7 maps with correct coordinates
- ✅ Applied Google Maps callback fix
- ✅ Created COORDINATE_DATA_SOURCE.md documentation

### Version 1.0 (Pre-November 2, 2025)
- Initial dashboard with 7 map visualizations
- Coordinate mismatch issues identified
- Manual coordinate overrides implemented

---

## Credits and Data Sources

### Data Sources
- **Statistics Canada 2021 Census** (Catalogue: 98-401-X2021013)
  - FSA population-weighted centroids
  - Socioeconomic data (income, Gini, indigenous, visible minority)
- **Google Distance Matrix API**
  - Driving distances via road network
- **Google Maps JavaScript API**
  - Interactive map visualization

### Generated With
- **Claude Code** (Anthropic)
  - Dashboard design and implementation
  - Data processing and visualization
  - Documentation and testing

### License
Research use only. Data sources subject to their respective licenses.

---

## Contact and Support

### For Questions About:
- **Data Sources**: See `COORDINATE_DATA_SOURCE.md`
- **Testing**: See `TESTING_INSTRUCTIONS.md`
- **Complete Fix History**: See `FIX_SUMMARY_COMPLETE.md` (parent directory)
- **Archive Files**: See `archive/README.md`

### Dashboard Status
- ✅ **Production Ready**
- ✅ **All 9 visualizations functional**
- ✅ **100% data integrity verified**
- ✅ **Comprehensive documentation complete**

---

**Last Updated**: November 2, 2025
**Dashboard Version**: 2.1 (Unified Dashboard)
**Total Visualizations**: 9
**Total FSAs**: 511
**Total DBS Centers**: 10
**Data Quality**: 100% (920 verified records)
**Coordinate Accuracy**: 99.2% authoritative

---

*This dashboard provides a comprehensive analysis of Deep Brain Stimulation access disparities across Canada, combining geographic, socioeconomic, and demographic data to inform healthcare policy and research.*
