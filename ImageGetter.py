from bing_image_downloader import downloader
import os

#deletes images that are jpegs, also returns number of jpegs found
def jpegRemove(query):
    root = "imagesROOT"
    deleteRoot = "imagesROOT\\"+query
    counter = 0
    for subdirectory, directory, images in os.walk(root):
        if subdirectory == deleteRoot:
            for image in images:
                extention = image[len(image)-4:]
                if extention == ".jpg":
                    counter+=1
                    os.remove(deleteRoot+"\\"+image)
        
    return counter

#filters through 
def filter(query):
    while(True):
        result = jpegRemove(query)
        if(result==0): 
            return
        downloader.download(query, limit=num+result,  output_dir="bin", adult_filter_off=False, force_replace=False, timeout=60, filter="transparent", verbose=True)
        root = "bin"
        i = 0
        for subdirectory, directory, images in os.walk(root):
            for image in images:
                i+=1
                if i<result:
                    os.remove(image)

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
