from bing_image_downloader import downloader
from PIL import Image, ImageEnhance
import os

#deletes files from given list of images
def deleteImage(imageList, root, query):
    for subdirectory, directory, images in os.walk(root):
        for image in images:
            if image in imageList:
                os.remove(root+"\\"+query+"\\"+image)
                imageList.remove(image)
                    
#deletes images that are more than 90% transparent
def transFind(query):
    root = "imagesROOT"
    findRoot = "imagesROOT\\"+query
    findCounter = 0
    deleteImages=[]
    for subdirectory, directory, images in os.walk(root):
        if subdirectory == findRoot:
            for image in images:
                totalCounter = 0
                transCounter = 0
                currImage = Image.open(subdirectory+"\\"+image)
                currImage = currImage.convert("RGBA")

                #define our pixel map
                pix = currImage.load()

                #iterate through our pixel map
                for y in range(currImage.size[1]):
                    for x in range(currImage.size[0]):
                        totalCounter+=1

                        #set our rgb values
                        red = pix[x,y][0]
                        green = pix[x,y][1]
                        blue = pix[x,y][2]
                        alpha = pix[x,y][3]
                        
                        #if alpha is 0 then it is transparent
                        if alpha == 0:
                            currImage.putpixel((x,y), (255, 255, 255, 255))
                            transCounter+=1
                        else:
                            currImage.putpixel((x,y), (0, 0, 0, 255))
                                            
                if transCounter == 0:
                    continue
                if transCounter/totalCounter >.9:
                    findCounter+=1
                    deleteImages.append(image)
    return findCounter, deleteImages

#deletes images that are jpegs, also returns number of jpegs found
def jpegFind(query):
    root = "imagesROOT"
    findRoot = "imagesROOT\\"+query
    counter = 0
    deleteImages=[]
    for subdirectory, directory, images in os.walk(root):
        if subdirectory == findRoot:
            for image in images:
                extention = image[len(image)-4:]
                if extention == ".jpg":
                    counter+=1
                    deleteImages.append(image)
        
    return counter, deleteImages

#filters through 
def filter(query):
    while(True):
        result = 0;
        resultJPEG, jpegList = jpegFind(query)
        resultTrans, transList = transFind(query)
        print("JPEG: ", resultJPEG)
        print("Transparent: ", resultTrans)
        if(resultJPEG==0 and resultTrans==0): 
            return

        #combine the two lists and give the combined list to delete function
        result = resultJPEG + resultTrans
        imageList = list(jpegList)
        imageList.extend(x for x in transList if x not in imageList)
        deleteImage(imageList, "imagesROOT", query)
        #get some new images
        downloader.download(query, limit=num+result,  output_dir="bin", adult_filter_off=False, force_replace=False, timeout=60, filter="transparent", verbose=True)

        #delete the entries that need deleted
        deleteImage(imageList, "bin", query)
                    
#main program
cont = True
while(cont):
    val = input("do you want to download more categories? (Y/N)   ")
    if val != "Y" and val != "y":
        cont = False
        continue
    query = input("What do you want images of?   ")
    num = int(input("How many images of "+ query + " do you want?   "))
    downloader.download(query, limit=num,  output_dir="imagesROOT", adult_filter_off=False, force_replace=False, timeout=60, filter="transparent", verbose=True) 
    filter(query)
