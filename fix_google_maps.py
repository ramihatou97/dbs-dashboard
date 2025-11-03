#!/usr/bin/env python3
"""
Fix Google Maps loading issues in all HTML files
Adds callback parameter and async/defer attributes
"""

import re
import os
from pathlib import Path

# Files to fix
HTML_FILES = [
    'map1_travel_burden_heatmap.html',
    'map2_vulnerability_index.html',
    'map3_indigenous_access_crisis.html',
    'map4_service_gaps_multibarrier.html',
    'map5_patient_flow_lines.html',
    'map5_patient_flow_enhanced.html',
    'distance_map.html',
    'combined_analysis.html'
]

def fix_google_maps_script(html_content, has_visualization=False):
    """
    Fix the Google Maps script tag to include callback and async/defer
    """
    # Pattern to match the existing Google Maps script tag
    old_pattern = r'<script src="https://maps\.googleapis\.com/maps/api/js\?key=([^"]+)">'

    # Replacement pattern with callback and async defer
    if has_visualization:
        # Keep existing libraries parameter and add callback
        new_script = r'<script async defer src="https://maps.googleapis.com/maps/api/js?key=\1&callback=initMap">'
    else:
        new_script = r'<script async defer src="https://maps.googleapis.com/maps/api/js?key=\1&callback=initMap">'

    # Replace the script tag
    html_content = re.sub(old_pattern, new_script, html_content)

    return html_content

def remove_window_onload(html_content):
    """
    Comment out window.onload = initMap; as it's redundant with callback parameter
    """
    # Pattern to match window.onload = initMap;
    pattern = r'(\s*)window\.onload\s*=\s*initMap;'
    replacement = r'\1// window.onload = initMap; // Removed: Using callback parameter instead'

    html_content = re.sub(pattern, replacement, html_content)

    return html_content

def fix_html_file(filepath):
    """
    Fix a single HTML file
    """
    print(f"\nProcessing: {filepath.name}")

    # Check if file has visualization library
    has_visualization = 'distance_map' in filepath.name or 'combined_analysis' in filepath.name

    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Create backup
        backup_path = filepath.with_suffix('.html.backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Backup created: {backup_path.name}")

        # Apply fixes
        original_content = content
        content = fix_google_maps_script(content, has_visualization)
        content = remove_window_onload(content)

        # Check if changes were made
        if content != original_content:
            # Write fixed content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Fixed: Added callback parameter and async/defer")
            print(f"  ✓ Fixed: Commented out window.onload")
            return True
        else:
            print(f"  ℹ No changes needed (already fixed or pattern not found)")
            return False

    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False

def main():
    print("=" * 80)
    print("GOOGLE MAPS FIX SCRIPT")
    print("=" * 80)
    print("\nThis script will:")
    print("1. Add 'async defer' attributes to Google Maps script tags")
    print("2. Add '&callback=initMap' parameter to API URLs")
    print("3. Comment out 'window.onload = initMap;'")
    print("4. Create .backup files for all modified files")

    # Get script directory
    script_dir = Path(__file__).parent

    print(f"\nWorking directory: {script_dir}")
    print(f"\nFiles to process: {len(HTML_FILES)}")

    # Process each file
    success_count = 0
    for filename in HTML_FILES:
        filepath = script_dir / filename

        if not filepath.exists():
            print(f"\n✗ File not found: {filename}")
            continue

        if fix_html_file(filepath):
            success_count += 1

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files processed: {len(HTML_FILES)}")
    print(f"Files modified: {success_count}")
    print(f"Files skipped: {len(HTML_FILES) - success_count}")

    if success_count > 0:
        print("\n✓ Fix completed successfully!")
        print("\nNext steps:")
        print("1. Open any map HTML file in your browser")
        print("2. Check if maps load correctly")
        print("3. If still errors, check Google Cloud Console:")
        print("   - Enable Maps JavaScript API")
        print("   - Enable Billing")
        print("   - Check API key restrictions")
        print("\n4. If you need to revert changes:")
        print("   - Backup files are saved as .html.backup")
        print("   - Simply rename them back to .html")
    else:
        print("\nℹ No files were modified.")

    print("=" * 80)

if __name__ == '__main__':
    main()
