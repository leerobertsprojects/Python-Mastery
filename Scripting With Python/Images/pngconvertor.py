import sys
from PIL import Image
from os import listdir, makedirs
folder = sys.argv[1]
new_folder = sys.argv[2]

def png_convertor(folder, new_folder):
    makedirs(f'{new_folder}', exist_ok=True)
    for file in listdir(folder):
        img = Image.open(f'{folder}/{file}')
        img.save(f"{new_folder}/{file.replace('.jpg', '')}.png", "png")


png_convertor(folder, new_folder)

