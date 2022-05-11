from PIL import Image
import glob, os, sys

# Script to save new rotated copies of images
# Usage: python3 rotate.py rotation "path"
# Example: python3 rotate.py 180 "music_instrument_images/Brass/Clarinet/"
# Make sure to have that last forward slash!

# Args from command line
degrees = int(sys.argv[1])
path = sys.argv[2]

# Get every jpg from named directory
for infile in glob.glob(path + "*.jpg"):
    file, ext = os.path.splitext(infile)    # Split file name from jpg extension
    with Image.open(infile) as im:
        im = im.rotate(degrees)             # Create new rotated image
        im.save(file + "rot" + str(degrees) + ext, "JPEG") # Save, with "rot[degrees]" appended
