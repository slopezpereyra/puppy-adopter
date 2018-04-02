#! /usr/bin/python3

""" This program scraps a user-given list of webpages to download images from. """

import os, requests, bs4, random, shutil, json

def get_cwd(appended_value):
    """Return the directory formed by the join of the working directory
    plus an appended value. Not a big deal, but makes things easier."""

    cwd = os.getcwd()
    cwd = cwd + appended_value

    return cwd

def save_pages_in_data(saves_list):

    """Saves the downloaded images into the data file. The downloaded images
    are a list of strings."""

    with open('data.txt', 'a') as outfile:
        json.dump(saves_list, outfile, ensure_ascii=False)

# List manipulation definitions

def get_list_from_data():

    """Reads the websites stored on listdata.txt to tell the program where
    to look and download from."""

    list_path = get_cwd('/listdata.txt')

    with open(list_path, 'r') as outfile:
        lecture = outfile.readlines()
        return lecture

# Scraping  and downloading definitions

def download_image(url, request_response):

    """Downloads an image from a given request. It names it the same as the
    requested url and saves it into the Puppies folder.

    The folder name in open(os.path.join(foldername)) etc. must be the same
    folder name stablished on the create_folder() function of setup.py """

    filename = url.split('/')[-1]
    with open(os.path.join('NameYourImageFolder', filename), 'wb') as image:
        shutil.copyfileobj(request_response.raw, image, [False])

def get_random_url(web_object, web_object_number):

    """Picks a random image from the the given website and retrieves its url.
    If it is a .jpg file, it returns the url after checking it wasn't
    downloaded before.

    There's a reason why I used if '.jpg' not in str(url_variable) instead of
    if str(url_variable).endswith('.jpg'): you'll find it on the look images
    function. """

    error_counter = 0

    while True:
        try:
            random_number = random.randint(0, web_object_number)
            url_variable = web_object[random_number].get('src')
            if '.jpg' not in str(url_variable):
                continue
            with open('data.txt') as data:
                lecture = data.read()
                if str(url_variable) in lecture:
                    print("Wasn't this image downloaded already...? Restarting...")
                    continue
                else:
                    return url_variable
        except IndexError:
            if error_counter < 5:
                print('Oops! Something went wrong. Starting again...')
                error_counter = error_counter + 1
                continue
            else:
                print("False returned.")
                return False


def look_images(pages_list, saves_list):

    """Iterates over each element of a websites list.
    For each of them it requests its url, it parses it with bsoup,
    selects all the images found and counts how many are they.

    Gets the url of one of those images randomly if it is not False
    (see the previous method to know in which case it would be) and
    beggins the download.

    There where cases of .jpg urls ending on ' 2x' and others of urls
    not beginning with 'https://'. Those errors are fixed before download.

    Once the url may have been fixed -if it was needed-, it is requested,
    appended to the saves_list and downloaded."""

    for i in pages_list:
        res = requests.get(i)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        soup_image = soup.select('img')
        image_count = len(soup_image)

        image_url = get_random_url(soup_image, image_count)
        if image_url is False:
            continue
        print("\n Images found...")
        print("\n Beginning download...")

        if str(image_url).endswith('.jpg 2x'):
            image_url = str(image_url.replace(' ', '')[:-2])
        if not str(image_url).startswith("http"):
            image_url = "https://" + str(image_url)
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        saves_list.append(str(image_url))
        download_image(image_url, response)
        print('Image downloaded!')

def get_page():

    """Joins all methods together after retrieving the list of websites to
    scrap and creating an alr_dow list -which stands for already downloaded-,
    which would be later stored to keep a register of which images have
    been downloaded already.

    You can make the for loop cycle as many times as you want, depending on
    how many images you want."""

    pages = get_list_from_data()
    alr_dow = []

    for x in range(0, 1):

        look_images(pages, alr_dow)
        save_pages_in_data(alr_dow)

get_page()
