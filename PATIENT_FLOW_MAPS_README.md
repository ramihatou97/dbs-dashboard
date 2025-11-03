# DBS Patient Flow Visualization Maps

Two new maps created to visualize the 920 individual patients and their DBS center choices.

## 📊 Map 1: Jittered Individual Patients
**File:** `map_patient_flow_jittered.html`

### Features:
- **920 colored dots** - one per patient/database row
- **Jittered placement** - dots scattered within ~5km of FSA centroid
- **10px medium dots** - balanced visibility for presentations
- **Color = Center used** - shows where each patient actually went

### Purpose:
- Visualize individual patient distribution
- Show overlapping patients from same FSA
- Reveal patterns where patients bypass closer centers

### Best for:
- Understanding patient-level flows
- Seeing density in urban areas
- Identifying outlier travel patterns

---

## 🥧 Map 2: FSA Pie Charts
**File:** `map_patient_flow_piechart.html`

### Features:
- **511 pie chart markers** - one per unique FSA
- **Pie size** - scaled by patient count (5-40px)
- **Color segments** - proportion going to each center
- **Clean aggregation** - easier to read at presentation scale

### Purpose:
- Show FSA-level catchment patterns
- Visualize multi-center FSAs clearly
- Cleaner for static presentations

### Best for:
- High-level overview
- Presentation slides
- Understanding FSA catchment splits

---

## 🎨 Color Palette (10 DBS Centers)

| Center | Color | Patients | % |
|--------|-------|----------|---|
| Toronto Western | #E63946 (Red) | 576 | 62.6% |
| London Health Sciences | #2A9D8F (Teal) | 70 | 7.6% |
| L'Enfant Jésus, Quebec | #F4A261 (Orange) | 57 | 6.2% |
| QEII Halifax | #264653 (Dark Blue) | 45 | 4.9% |
| CHUM Montreal | #E76F51 (Coral) | 36 | 3.9% |
| Ottawa Civic | #8338EC (Purple) | 36 | 3.9% |
| Alberta Hospital | #06FFA5 (Mint) | 30 | 3.3% |
| Royal Saskatoon | #FFB703 (Gold) | 30 | 3.3% |
| Foothills Calgary | #023E8A (Navy) | 29 | 3.2% |
| Sherbrooke | #BC6C25 (Brown) | 11 | 1.2% |

---

## 📥 Export Features

Both maps include:
- **PNG Download** - High-res 2x scale for presentations
- **PDF Download** - Vector format for editing
- **Interactive legend** - All 10 centers with patient counts
- **Click tooltips** - Details on hover/click

---

## 🔍 Key Insights Visible

### Multi-Center FSAs (28 FSAs)
Examples from the data:
- **K0K**: 4 to Toronto, 1 to London
- **N0E**: 4 to Toronto, 2 to London  
- **L7M**: 4 to Toronto, 3 to London

### Patient Choice Patterns:
- Most patients use nearest center
- Some bypass closer centers (referral patterns, expertise)
- Urban FSAs show higher diversity
- Rural FSAs typically single-center

---

## 📁 Data Sources

- **Database:** `database-03-11-25.xlsx` (920 patients)
- **FSA Coordinates:** From existing map files
- **Center Coordinates:** 10 DBS facilities across Canada

---

## 💡 Usage Tips

**For Presentations:**
1. Use **Pie Chart map** for overview slides
2. Use **Jittered map** for detailed analysis
3. Download as PNG at 2x resolution
4. Legend is presentation-ready (14px font)

**For Analysis:**
1. Click individual dots/pies for details
2. Zoom to specific regions
3. Compare with distance/vulnerability maps
4. Export to PDF for reports

---

Generated: November 3, 2025
Data: 920 patients across 511 FSAs and 10 DBS centers
