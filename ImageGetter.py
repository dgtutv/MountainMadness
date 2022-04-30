from google_images_search import GoogleImagesSearch

#Define our google images identity
gis = GoogleImagesSearch('GCS_DEVELOPER_KEY', 'GCS_CX')

#Ask user if they want more images, and if so, what and how many
cont = True
while(cont):
    val = input("do you want to download more categories? (Y/N)   ")
    if val != "Y" and val != "y":
        cont = False
        continue
    query = input("What do you want images of?   ")
    num = int(input("How many "+ query + "'s do you want?   "))

    #define our search parameters
    _search_params = {
        'q': '...',
        'num': 10,
        'fileType': 'jpg|png', 
        'imgDominantColor': 'green', 
    }

    #Actually search
    gis.search(search_params=_search_params, path_to_dir='imagesROOT')
    
