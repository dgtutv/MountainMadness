import numpy
from PIL import Image, ImageEnhance
import os



root = "imagesROOT"
for subdirectory, directory, images in os.walk(root):
    for image in images:
        print(image)
        currImage = Image.open(subdirectory+"\\"+image)
        currImage = currImage.convert("RGBA")

        #define our pixel map
        pix = currImage.load()

        #iterate through our pixel map
        for y in range(currImage.size[1]):
            for x in range(currImage.size[0]):

                #set our rgb values
                red = pix[x,y][0]
                green = pix[x,y][1]
                blue = pix[x,y][2]
                alpha = pix[x,y][3]
                
                #if alpha is 0 then it is transparent
                if alpha == 0:
                    currImage.putpixel((x,y), (255, 255, 255, 255))
                else:
                    currImage.putpixel((x,y), (0, 0, 0, 255))

        #save the image
        currImage.save(subdirectory+"\\"+"dark-"+image)
