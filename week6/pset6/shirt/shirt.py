import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) > 3: # Check for valid cmd #
    sys.ext("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.ext("Too few command-line arguments")

ext1 = splitext(sys.argv[1]) # get input image extension
ext2 = splitext(sys.argv[2])

if ext2[1] not in [".jpg", ".jpeg", ".png"]: # Varify input/output ext
    sys.exit("Invalid output")
if ext1[1] != ext2[1]:
    sys.exit("Input and output have different extensions")

try:
    input = Image.open(sys.argv[1]) # open input image
except FileNotFoundError:
    sys.exit("Input does not exist")

im = Image.open("shirt.png")
input = ImageOps.fit(input, im.size) # resized input image

input.paste(im, im)
input.save(sys.argv[2])