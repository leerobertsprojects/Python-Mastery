import os
from PIL import Image, ImageFilter
basedir = os.path.dirname(__file__)
img = Image.open(f'{basedir}/pokedex/bulbasaur.jpg')
filtered_image = img.convert('L')
filtered_image.save(f"{basedir}/grey.png", "png")
print(basedir)
# print(img.format)
# print(img.size)
# print(img.mode)


