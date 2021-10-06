import PIL
from PIL import Image
import os
import sys

print('\n    *****  Image Compressor  ****\n')

# use sys module to grab the first and 2nd argument from cmd
media = sys.argv[1]
output = sys.argv[2]

# check if output folder exists, if not create one
if not os.path.exists(output):
    os.makedirs(output)

# input width/Height
width = int(input("Input Width: "))
height = int(input("Input height: "))

try:
    # loop through each item of media folder
    for filename in os.listdir(media):
        # Grab/Access images in Media Folder
        img = Image.open(f'{media}{filename}')
        # clean name (remove jpg at the end of filename)
        clean_name = os.path.splitext(filename)[0]

        # Resize an Images using thumbnail()
        img.thumbnail((width, height), PIL.Image.ANTIALIAS)

        # Save and Convert a resize images
        img.save(f'{output}{clean_name}.png', 'png', optimize=True, quality=95)

    # loop through each item of output folder
    for filename in os.listdir(output):
        clean_name = os.path.splitext(filename)[0]
        print(f'{clean_name} compressed successfully!')

    print('\nThank you for using Our Image Compressor!\n')

except ValueError:
    print("Please enter numbers only!")
