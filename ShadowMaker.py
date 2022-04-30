from PIL import Image, ImageEnhance
import os

root = "imagesROOT"
for subdirectory, directory, images in os.walk(root):
    for image in images:
        print(image)
        currImage = Image.open(subdirectory+"\\"+image)
        modifier = ImageEnhance.Brightness(currImage)
        output = modifier.enhance(0)
        output.save("dark-"+image)
