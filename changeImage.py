import os
from PIL import Image

"""
Image Processing (changeImage.py)
Goal: Process raw images from ~/supplier-data/images/.
Specs:
    Size: Resize to 600x400 pixels.
    Format: Convert from .TIFF to .JPEG.
    Mode: Convert RGBA to RGB first.
Next Step: Upload them using supplier_image_upload.py to http://[linux-instance-external-IP]/upload/.
"""

SOURCE = "~/supplier-data.images"
DEST = "http://[linux-instance-external-IP]/upload/"

def process(file):
    img = Image.open(file)
    print(f" [IMG] Converting {img.format} from {img.mode} to .JPEG (600x400)...")
    img = img.resize((600, 400))
    img = img.convert("RGB")
    return img

def main():
    for image in os.listdir(os.path.expanduser(SOURCE)):
        if image.endswith(".tiff"):
            fp = os.path.join(os.path.expanduser(SOURCE), image)
            processed_image = process(fp)
            # Save the processed image as JPEG
            processed_image.save(os.path.join(os.path.expanduser(SOURCE), image.replace(".tiff", ".jpeg")))

if __name__ == "__main__":
    main()

