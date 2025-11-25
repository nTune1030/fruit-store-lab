#!/usr/bin/env python3

from pathlib import Path
from PIL import Image

"""
changeImage.py
--------------
Goal: Process raw images from ~/supplier-data/images/.
Specs: Resize to 600x400, Format: .JPEG, Mode: RGB.
"""

SOURCE_DIR = Path.home() / "supplier-data/images"

def process_image(file_path):
    """
    Opens an image, resizes, converts, and saves as JPEG.
    Save them in the same path ~/supplier-data/images, with a JPEG extension.
    """
    try:
        with Image.open(file_path) as img:

            # image.tiff -> image.jpeg
            new_path = file_path.with_suffix('.jpeg')

            print(f" [IMG] Processing {file_path.name} -> {new_path.name}")

            img.resize((600, 400)).convert("RGB").save(new_path, "JPEG")
            
    except OSError as e:
        print(f"Error processing {file_path.name}: {e}")

def main():
    if not SOURCE_DIR.exists():
        print(f"Error: Directory {SOURCE_DIR} does not exist.")
        return

    for file_path in SOURCE_DIR.glob("*.tiff"):
        process_image(file_path)

    # Incase file extension is not .tiff (eg. tif, TIFF, ...)
    # Iterates over everything and filters inside
    # for file_path in SOURCE_DIR.iterdir():
    #     if file_path.suffix.lower() == ".tiff":
    #         process_image(file_path)

if __name__ == "__main__":
    main()