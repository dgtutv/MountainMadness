from PIL import Image
from os import listdir

root = "C:
for directory in directories:
    for i in os.listdir(directory):
        currImage = Image.open(image)
        modifier = ImageEnhance.Brightness(currImage)
        output = modifier.enhance(0)
        output.save(image.filename+"-dark")
