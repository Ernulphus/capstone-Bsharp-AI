import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder):
    # creating a folder for the images to be saved into
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        # else do nothing
        pass
    #change directory to the new folder
    os.chdir(os.path.join(os.getcwd(), folder))

    # requesting the url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # seeing if access is forbidden or not
    print(soup.title.text)

    # using beautiful soup to find everything with the tag 'img'
    images = soup.find_all('img')

    # iterating through the webpage, retriving identifying 
    # the tags and writing them to the folder
    for i in images:
        name = i['alt'] # tag containing the image name
        link = i['src'] # tag containing the image link
        # using open function to open the folder
        with open(name.replace(' ', '-').replace('/','') + '.jpg', 'wb') as f:
            image = requests.get(link)
            f.write(image.content)
            print('Writing: ', name)


download_images('https://www.gettyimages.com/photos/musical-instrument', 'instrument images')
