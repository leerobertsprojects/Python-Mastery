import os
from PIL import Image, ImageFilter
# basedir = os.path.dirname(__file__)
# img = Image.open(f'{basedir}/pokedex/bulbasaur.jpg')
# filtered_image = img.convert('L')
# new_img = filtered_image.resize((400, 400))
# new_img.save(f"{basedir}/resize.png", "png")
# box = (100, 100, 400, 400)
# region = filtered_image.crop(box)
# region.save(f"{basedir}/region.png", "png")

basedir = os.path.dirname(__file__)
img = Image.open(f'{basedir}/tech.jpg')
img.thumbnail((400, 400))
img.save(f"{basedir}/tech.png", "png")
print(img.size)

