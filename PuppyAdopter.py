#! /usr/bin/python3

"""This program downloads images from a user-given list of websites."""

import os
import pickle
import random
import shutil

import requests
import bs4

def save_image(url, request_response, env_data):
    """Downloads an image from a given request. It names it the same as the
    requested url and saves it into the Puppies folder.
    The folder name in open(os.path.join(foldername)) etc. must be the same
    folder name stablished on the create_folder() function of setup.py """

    filename = url.split('/')[-1]
    with open(os.path.join(env_data.folder, filename), 'wb') as image:
        shutil.copyfileobj(request_response.raw, image, [False])


def get_random_image(web_object, web_object_number, env_data):
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
            with open(env_data.datafile) as data:
                lecture = data.read()
                if str(url_variable) in lecture:
                    print("Wasn't this image downloaded already? Restarting...")
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


def look_for_images(pages_list, saves_list, env_data):
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
        soup_image = bs4.BeautifulSoup(res.text, "html.parser").select('img')
        image_count = len(soup_image)

        image_url = get_random_image(soup_image, image_count, env_data)
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
        save_image(image_url, response, env_data)
        print('Image downloaded!')


def download_images():
    """ This is the main function.
    Loops over all existing environments and downloads images on them
    from the web sites of the environment in question. Keeps track of the
    downloaded files and stores them on the environment's data through the
    alr_dow list -which stands for 'already downloaded'-, keeping a register
    of which images have been downloaded already.
    data, and which registers what images have been downloaded already."""

    with open("environmentor_data", "rb") as f:
        for datamanager in pickle.load(f):
            print("Downloading to " + datamanager.environment)
            if os.path.isdir(datamanager.folder):  # If folder wasn't erased...
                pages = datamanager.get_pages_list()
                alr_dow = []
                for X in range(0, 5):
                    look_for_images(pages, alr_dow, datamanager)
                    datamanager.save_pages_in_data(alr_dow)
                print("Finished")
            else:
                print("""ERROR: download attempt on unexisting environment; moving
                to the following.""")
                continue


download_images()
