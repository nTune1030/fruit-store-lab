#!/usr/bin/env python3

import requests

"""
Takes jpeg images from the supplier-data/images directory and 
uploads them to the web server fruit catalog.
"""

url = "http://localhost/upload/"
# TODO: Iterate through converted .jpeg files (changeImage.py) 
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})