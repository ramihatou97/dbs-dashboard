#!/usr/bin/env python3
"""
Script to add download buttons to all map/visualization HTML files in the public_dashboard.
Adds html2canvas and jsPDF libraries, styled download buttons, and download functionality.
"""

import os
import re

# Define the files to modify
GOOGLE_MAPS_FILES = [
    'map1_travel_burden_heatmap.html',
    'map2_vulnerability_index.html',
    'map3_indigenous_access_crisis.html',
    'map4_service_gaps_multibarrier.html',
    'map5_patient_flow_lines.html',
    'map5_patient_flow_enhanced.html',
    'distance_map.html',
    'combined_analysis.html',
]

PLOTLY_FILES = [
    'patient_flow_sankey.html',
    'provincial_comparison.html',
    'comprehensive_dashboard_final.html',
]

# CDN scripts to add
CDN_SCRIPTS = """    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>"""

# CSS styles for download buttons
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

# HTML for download buttons (Google Maps version)
DOWNLOAD_BUTTONS_HTML_GMAPS = """
    <!-- Download Buttons -->
    <div class="download-buttons">
        <button class="download-btn" onclick="downloadMapPNG()">
            <span>📥</span> Download PNG
        </button>
        <button class="download-btn" onclick="downloadMapPDF()">
            <span>📄</span> Download PDF
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

        async function downloadMapPNG() {
            showOverlay();
            try {
                const mapDiv = document.body;
                const canvas = await html2canvas(mapDiv, {
                    useCORS: true,
                    scale: 2,
                    backgroundColor: '#ffffff',
                    logging: false
                });

                const link = document.createElement('a');
                const filename = document.title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
                link.download = `${filename}_${new Date().toISOString().split('T')[0]}.png`;
                link.href = canvas.toDataURL('image/png');
                link.click();

                hideOverlay();
            } catch (error) {
                console.error('Download failed:', error);
                alert('Download failed. Please try again.');
                hideOverlay();
            }
        }

        async function downloadMapPDF() {
            showOverlay();
            try {
                const mapDiv = document.body;
                const canvas = await html2canvas(mapDiv, {
                    useCORS: true,
                    scale: 2,
                    backgroundColor: '#ffffff',
                    logging: false
                });

                const { jsPDF } = window.jspdf;
                const pdf = new jsPDF('landscape', 'mm', 'a4');

                const imgData = canvas.toDataURL('image/png');
                const pdfWidth = pdf.internal.pageSize.getWidth();
                const pdfHeight = pdf.internal.pageSize.getHeight();
                pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);

                const filename = document.title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
                pdf.save(`${filename}_${new Date().toISOString().split('T')[0]}.pdf`);

                hideOverlay();
            } catch (error) {
                console.error('PDF generation failed:', error);
                alert('PDF generation failed. Please try again.');
                hideOverlay();
            }
        }
    </script>"""


def add_cdn_scripts(html_content):
    """Add CDN scripts after Google Maps API script or in head section"""
    # Try to add after Google Maps API script
    if 'maps.googleapis.com' in html_content:
        pattern = r'(<script src="https://maps\.googleapis\.com/[^"]+"></script>)'
        if re.search(pattern, html_content):
            html_content = re.sub(pattern, r'\1\n' + CDN_SCRIPTS, html_content, count=1)
            return html_content

    # Otherwise add before closing </head>
    html_content = html_content.replace('</head>', CDN_SCRIPTS + '\n</head>', 1)
    return html_content


def add_download_styles(html_content):
    """Add download button styles before closing </style> tag"""
    html_content = html_content.replace('    </style>', DOWNLOAD_STYLES + '\n    </style>', 1)
    return html_content


def add_download_buttons(html_content):
    """Add download buttons HTML and JavaScript before closing </body> tag"""
    html_content = html_content.replace('</body>', DOWNLOAD_BUTTONS_HTML_GMAPS + '\n</body>', 1)
    return html_content


def process_google_maps_file(filepath):
    """Process a Google Maps HTML file to add download functionality"""
    print(f"Processing Google Maps file: {os.path.basename(filepath)}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has download buttons
    if 'downloadMapPNG' in content:
        print(f"  ✓ Already has download buttons, skipping...")
        return False

    # Add CDN scripts
    content = add_cdn_scripts(content)

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
    print("Adding Download Buttons to Dashboard Maps")
    print("=" * 60)
    print()

    modified_count = 0
    skipped_count = 0

    # Process Google Maps files
    print("Processing Google Maps files...")
    for filename in GOOGLE_MAPS_FILES:
        filepath = os.path.join('/Users/ramihatoum/Desktop/PPA/maps/public_dashboard', filename)
        if os.path.exists(filepath):
            if process_google_maps_file(filepath):
                modified_count += 1
            else:
                skipped_count += 1
        else:
            print(f"  ✗ File not found: {filename}")

    print()
    print("=" * 60)
    print(f"Summary: {modified_count} files modified, {skipped_count} skipped")
    print("=" * 60)
    print()
    print("Note: Plotly files will be handled separately with native Plotly download")


if __name__ == '__main__':
    main()
