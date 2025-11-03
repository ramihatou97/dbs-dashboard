# Archive Directory - Public Dashboard

This directory contains archived files from the public_dashboard cleanup performed on November 2, 2025.

## Purpose

Files in this directory are no longer actively used in the main dashboard but are preserved for reference and rollback purposes.

## Archived Files

### Backup Files (8 files, ~1 MB total)
Created during Google Maps callback fix on November 2, 2025:

1. **combined_analysis.html.backup** (232K) - Backup before callback fix
2. **distance_map.html.backup** (115K) - Backup before callback fix
3. **map1_travel_burden_heatmap.html.backup** (112K) - Backup before callback fix
4. **map2_vulnerability_index.html.backup** (122K) - Backup before callback fix
5. **map3_indigenous_access_crisis.html.backup** (138K) - Backup before callback fix
6. **map4_service_gaps_multibarrier.html.backup** (127K) - Backup before callback fix
7. **map5_patient_flow_enhanced.html.backup** (108K) - Backup before callback fix
8. **map5_patient_flow_lines.html.backup** (106K) - Backup before callback fix

### Old/Unused Files (4 files, ~9.2 MB total)

1. **index_OLD.html** (8.1K)
   - Previous version of the main dashboard
   - Archived: November 2, 2025
   - Reason: Replaced by updated index.html with corrected coordinate metadata

2. **patient_flow_sankey.html** (4.6M)
   - Sankey diagram visualization of patient flows
   - Archived: November 2, 2025
   - Reason: Not referenced in main dashboard index.html

3. **provincial_comparison.html** (4.6M)
   - Provincial comparison visualization
   - Archived: November 2, 2025
   - Reason: Not referenced in main dashboard index.html

4. **map5_patient_flow_enhanced.html** (108K)
   - Alternate version of patient flow visualization
   - Archived: November 2, 2025
   - Reason: Not used; map5_patient_flow_lines.html is the active version

## Restoration

If you need to restore any of these files:

1. Copy the file from this archive directory
2. Move it to the parent directory (`public_dashboard/`)
3. Update index.html if needed to reference the restored file

## Backup Files

The `.backup` files are pre-Google Maps fix versions. They can be safely deleted after verifying that all maps load correctly with the callback fix applied.

## Cleanup History

- **Date**: November 2, 2025
- **Reason**: Organize public_dashboard directory and remove clutter
- **Files Archived**: 12 total files
- **Space Saved**: ~10.2 MB moved to archive
- **Active Files Remaining**: 15 files in main directory

## Current Dashboard Status

The active dashboard (`index.html`) now includes:
- 7 interactive maps (maps 1-5, distance_map, combined_analysis)
- Corrected Statistics Canada coordinates (99.2% coverage)
- Google Distance Matrix API driving distances
- Updated metadata showing correction date
- All maps verified and functional

---

**Archive Created**: November 2, 2025
**Created By**: Claude Code cleanup automation
**Dashboard Version**: v2.0 (Population Centroid Alignment)
