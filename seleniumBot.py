#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless") # Run in headless mode
# StackOverflow said this configuration would fix an error I'm getting on Linux:
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
from PIL import Image
import requests
import io
import time
import datetime
import sys
#setting up the path for web driver find the executable
path = "/root/chromedriver"
wd = webdriver.Chrome(path, options=chrome_options)

# Set up instrument type to save it as and the url for that google search
instrument_type = "Piano" # First letter capitalized, singular (except Bagpipes)

url = str(sys.argv[1])

#writing a function to get images from the webpage before we download them
def get_images(wd, delay, max_images):

    #writing a nested function that allows us to scroll down to the end of the page so all content is already loaded
    def scroll_down(wd):

        #executing a javascript script to scroll down the page
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    #getting our specified webpage
    wd.get(url)

    #making sure we don't have duplicate urls using the set function
    image_urls = set()

    skips = 0

    #while the number if images is less than the max number of images specified, we will continue
    while len(image_urls) + skips < max_images:

        #calling the function, using the webdriver to scroll to the bottom of the screen
        scroll_down(wd)

        #making our thumbnails equal to the value the class names that all the images are given on the webpage
        #this will give me any tags wth this class name
        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        #writing a for loop we don't keep getting the same image
        for img in thumbnails[len(image_urls) + skips: max_images]:
            try:
                #click on the image
                img.click()
                #wait a second before continuing
                time.sleep(delay)
            except:
                continue
            #getting the enlarged images in google
            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
            for i in images:
                if i.get_attribute('src') in image_urls:
                    # max_images += 1
                    skips += 1
                    break

                #if we have a source tag and then http is in that source tag
                if i.get_attribute('src') and 'http' in i.get_attribute('src'):
                    #add the proper image with a valid link to image_urls
                    image_urls.add(i.get_attribute('src'))
                    print(f"found {len(image_urls)}")
        
        # Check if we've reached the end
        try:
            wd.find_element(by=By.XPATH, value="// a[contains(text().\'you've reached the end')]")
            break
        except:
            continue

        # Check if we need to load more images
        try: 
            wd.find_element(by=By.XPATH, value="// a[contains(text().\'Show more results')]").click()
        except:
            continue

    return image_urls

#writng a function to download the image for a webpage
def download_image(download_path, url, file_name):
    try:
        #making an http request to get the content of the specified image
        image_content = requests.get(url).content

        #saving the image content into memory as bytes
        image_file = io.BytesIO(image_content)

        #using the Pillow library to load the bytes from memory as an image
        img = Image.open(image_file)

        #generating the file path to open up below
        file_path = download_path + file_name

        #opening the filepath and using wb to write bytes or write an image
        with open(file_path, "wb") as f:
            #saving the the image to f as a JPEG format
            img.save(f, "JPEG")
    except Exception as e:
        print('Failed - ', e)

    print("Success")

urls = get_images(wd, 0, 300) # Get images using wd, 2nd param is delay, 3rd is number of images to get

#looping through the different urls we have
for i, url in enumerate(urls):
    #downloading to the instrument_images folder with the .jpg format and date in ms
    download_image("music_instruments_images/Percussion/" + instrument_type+"/", url, instrument_type + datetime.datetime.now().strftime("%f") + ".jpg")

#closing the chrome window so we don't have a bunch webpages open was we are done downloading the images
wd.quit()
