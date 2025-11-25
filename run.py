#!/usr/bin/env python3

"""
Fruit Catalog Description Uploader
----------------------------------
This script parses unstructured text descriptions of fruits and uploads them 
to the web server via a REST API.

Key Functions:
- Scans ~/supplier-data/descriptions/ for .txt files.
- Parses the file content (Line 1: Name, Line 2: Weight, Line 3: Description).
- Cleans the weight data (removes "lbs" and converts to integer).
- Associates the text file with its corresponding image (e.g., 001.txt -> 001.jpeg).
- POSTs the structured JSON payload to the Django API endpoint.

Dependencies:
- requests: To handle the HTTP POST interaction.
- os: For file system traversal and path management.

Usage:
    ./run.py
"""

import os
import requests


# Using localhost because this runs ON the web server machine
BASE_URL = "http://localhost/fruits/"
DESC_PATH = os.path.expanduser('~/supplier-data/descriptions/')

def process_descriptions():
    files = [f for f in os.listdir(DESC_PATH) if f.endswith('.txt')] # Get all text files
    
    print(f"Found {len(files)} descriptions to process.")

    for file in files:
        with open(os.path.join(DESC_PATH, file), 'r') as f:
            lines = f.readlines()
            
            # Parse the data (Format is strict: Name, Weight, Desc)
            fruit_name = lines[0].strip() # remove the newline characters \n
            fruit_weight = int(lines[1].strip().replace(" lbs", ""))
            fruit_desc = lines[2].strip()
            
            # Map the image filename
            image_name = file.replace(".txt", ".jpeg") # Logic: 001.txt -> 001.jpeg
            
            # Construct the JSON payload
            fruit_data = {
                "name": fruit_name,
                "weight": fruit_weight,
                "description": fruit_desc,
                "image_name": image_name
            }
            
            # POST to the API
            try:
                response = requests.post(BASE_URL, json=fruit_data)
                if response.status_code == 201:
                    print(f"✔ Uploaded: {fruit_name}")
                else:
                    print(f"❌ Failed {fruit_name}: {response.status_code}")
            except Exception as e:
                print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    process_descriptions()