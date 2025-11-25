#!/usr/bin/env python3

"""
Supplier Image Upload Script
----------------------------
This script iterates through processed JPEG images in the supplier-data directory
and uploads them to the Fruit Catalog web server via a POST request.

Key Features:
- Scans ~/supplier-data/images/ for .jpeg files.
- Uploads each file to http://localhost/upload/.
- Reports success (201 Created) or failure for each file.

Dependencies:
- requests: For handling HTTP POST operations.
- pathlib: For file path manipulation.

Usage:
    ./supplier_image_upload.py
"""

import requests
from pathlib import Path

# URL explicitly set to localhost as per lab configuration
url = "http://localhost/upload/"

# Define the path using pathlib
IMAGE_DIR = Path.home() / "supplier-data/images"

def upload_images():
    # 1. Iterate through all JPEG files
    images = list(IMAGE_DIR.glob('*.jpeg'))
    
    if not images:
        print(f"No JPEG images found in {IMAGE_DIR}. Did you run changeImage.py?")
        return

    for image_path in images:
        print(f"Uploading {image_path.name}...")
        
        # 2. Open the file in binary read mode ('rb')
        with open(image_path, 'rb') as opened_file:
            
            # 3. Send the POST request
            try:
                # The API expects the file in the 'file' field
                response = requests.post(url, files={'file': opened_file}, timeout=10)
                
                # 4. Check status
                if response.status_code == 201:
                    print("   [OK] Success!")
                else:
                    print(f"   [FAIL] Status Code: {response.status_code}")
            
            except Exception as e:
                print(f"   [ERROR] Could not upload: {e}")

if __name__ == "__main__":
    upload_images()