#!/usr/bin/env python3
"""
Script to add download buttons to Plotly visualization HTML files.
Uses Plotly's native download functionality for high-quality PNG and SVG exports.
"""

import os
import re

# Define the Plotly files to modify
PLOTLY_FILES = [
    'patient_flow_sankey.html',
    'provincial_comparison.html',
    'comprehensive_dashboard_final.html',
]

# CSS styles for download buttons (matching Google Maps style)
DOWNLOAD_STYLES = """
        /* Download Button Styles */
        .download-buttons {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            display: flex;
            gap: 10px;
        }
        .download-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .download-btn:active {
            transform: translateY(0);
        }
        .loading-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 9999;
            justify-content: center;
            align-items: center;
        }
        .loading-content {
            background: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 16px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }"""

# HTML for download buttons (Plotly version)
DOWNLOAD_BUTTONS_HTML_PLOTLY = """
    <!-- Download Buttons -->
    <div class="download-buttons">
        <button class="download-btn" onclick="downloadPlotlyPNG()">
            <span>📥</span> Download PNG
        </button>
        <button class="download-btn" onclick="downloadPlotlySVG()">
            <span>🎨</span> Download SVG
        </button>
    </div>

    <!-- Loading Overlay -->
    <div class="loading-overlay" id="loadingOverlay">
        <div class="loading-content">
            <div class="spinner"></div>
            <p>Generating download...</p>
        </div>
    </div>

    <script>
        function showOverlay() {
            document.getElementById('loadingOverlay').style.display = 'flex';
        }

        function hideOverlay() {
            document.getElementById('loadingOverlay').style.display = 'none';
        }

        function getPlotlyDiv() {
            // Find the plotly graph div
            const divs = document.getElementsByClassName('plotly-graph-div');
            return divs.length > 0 ? divs[0] : null;
        }

        function downloadPlotlyPNG() {
            showOverlay();
            try {
                const plotDiv = getPlotlyDiv();
                if (!plotDiv) {
                    alert('Could not find Plotly visualization');
                    hideOverlay();
                    return;
                }

                const filename = (document.title || 'plotly_chart').replace(/[^a-z0-9]/gi, '_').toLowerCase();
                const date = new Date().toISOString().split('T')[0];

                Plotly.downloadImage(plotDiv, {
                    format: 'png',
                    width: 1920,
                    height: 1080,
                    scale: 2,  // 2x for high resolution (effective 3840x2160)
                    filename: `${filename}_${date}`
                }).then(function() {
                    hideOverlay();
                }).catch(function(err) {
                    console.error('Download failed:', err);
                    alert('Download failed. Please try again.');
                    hideOverlay();
                });
            } catch (error) {
                console.error('Download failed:', error);
                alert('Download failed. Please try again.');
                hideOverlay();
            }
        }

        function downloadPlotlySVG() {
            showOverlay();
            try {
                const plotDiv = getPlotlyDiv();
                if (!plotDiv) {
                    alert('Could not find Plotly visualization');
                    hideOverlay();
                    return;
                }

                const filename = (document.title || 'plotly_chart').replace(/[^a-z0-9]/gi, '_').toLowerCase();
                const date = new Date().toISOString().split('T')[0];

                Plotly.downloadImage(plotDiv, {
                    format: 'svg',
                    width: 1920,
                    height: 1080,
                    filename: `${filename}_${date}`
                }).then(function() {
                    hideOverlay();
                }).catch(function(err) {
                    console.error('SVG download failed:', err);
                    alert('SVG download failed. Please try again.');
                    hideOverlay();
                });
            } catch (error) {
                console.error('SVG download failed:', error);
                alert('SVG download failed. Please try again.');
                hideOverlay();
            }
        }
    </script>"""


def add_download_styles(html_content):
    """Add download button styles in the head section"""
    # Add <head> if it doesn't exist
    if '<head>' not in html_content:
        html_content = html_content.replace('<html>', '<html>\n<head>\n<style>' + DOWNLOAD_STYLES + '\n</style>\n</head>', 1)
    # If head exists but no style tag
    elif '<style>' not in html_content:
        html_content = html_content.replace('</head>', '<style>' + DOWNLOAD_STYLES + '\n</style>\n</head>', 1)
    # If style tag exists
    else:
        html_content = html_content.replace('</style>', DOWNLOAD_STYLES + '\n</style>', 1)

    return html_content


def add_download_buttons(html_content):
    """Add download buttons HTML and JavaScript before closing </body> tag"""
    html_content = html_content.replace('</body>', DOWNLOAD_BUTTONS_HTML_PLOTLY + '\n</body>', 1)
    return html_content


def process_plotly_file(filepath):
    """Process a Plotly HTML file to add download functionality"""
    print(f"Processing Plotly file: {os.path.basename(filepath)}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has download buttons
    if 'downloadPlotlyPNG' in content:
        print(f"  ✓ Already has download buttons, skipping...")
        return False

    # Add styles
    content = add_download_styles(content)

    # Add download buttons and functionality
    content = add_download_buttons(content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Added download buttons successfully")
    return True


def main():
    print("=" * 60)
    print("Adding Download Buttons to Plotly Visualizations")
    print("=" * 60)
    print()

    modified_count = 0
    skipped_count = 0
    missing_count = 0

    # Process Plotly files
    print("Processing Plotly files...")
    for filename in PLOTLY_FILES:
        filepath = os.path.join('/Users/ramihatoum/Desktop/PPA/maps/public_dashboard', filename)
        if os.path.exists(filepath):
            if process_plotly_file(filepath):
                modified_count += 1
            else:
                skipped_count += 1
        else:
            print(f"  ✗ File not found: {filename}")
            missing_count += 1

    print()
    print("=" * 60)
    print(f"Summary: {modified_count} files modified, {skipped_count} skipped, {missing_count} missing")
    print("=" * 60)
    print()
    print("Note: Plotly download uses native Plotly.downloadImage() for high-quality PNG and vector SVG exports")


if __name__ == '__main__':
    main()
