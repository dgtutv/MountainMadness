from bing_image_downloader import downloader

cont = True
while(cont):
    val = input("do you want to download more categories? (Y/N)   ")
    if val != "Y" and val != "y":
        cont = False
        continue
    query = input("What do you want images of?   ")
    num = int(input("How many images of "+ query + " do you want?   "))
    downloader.download(query, limit=num,  output_dir="imagesROOT", adult_filter_off=False, force_replace=False, timeout=60, filter="transparent", verbose=True) 
