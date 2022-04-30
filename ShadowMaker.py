import ImageGetter

from PIL import Image, ImageEnhance
import os

root = "imagesROOT"
for subdirectory, directory, images in os.walk(root):
    for image in images:
        print(image)
        currImage = Image.open(subdirectory+"\\"+image)
        currImage = currImage.convert("RGBA")
        gray = currImage.convert('L')
        bw = gray.point(lambda x: 0 if x!=255 else 255, '1')
        bw.save(subdirectory+"\\"+"dark-"+image)
