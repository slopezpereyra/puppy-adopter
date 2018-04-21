#! /usr/bin/python3

"""This program downloads images from a user-given list of websites."""

import json
import os
import pickle
import random
import shutil

import bs4
import requests


class EnvironmentSetup:

    """Creates the basic folders and files an environment will manage data on.
    An environment is simply a place in your system in which, and with which
    elements, a program operates. You can have many environments for this program:
    W'riters' may be dedicated to downloading writers' pictures; Puppies,
    puppies' pictures, and so."""

    def __init__(self):
        self.env_folder = self.create_environment_folder()
        self.image_folder = self.create_image_folder()
        self.data = self.create_data_file()
        self.list_data = self.create_list_data()

    # CWD function definition.

    @staticmethod
    def get_cwd(appended_value):
        """Returns the current working directory with the chance of adding
        an aditional direction. Not a big deal, but makes things easier."""
        cwd = os.getcwd()
        cwd += appended_value
        return cwd

    # Environment setting definitions

    def create_environment_folder(self):
        """Creates an environment folder"""
        name = 'Environment'

        if os.path.isdir(self.get_cwd("/" + name)) is False:
            os.makedirs(self.get_cwd('/' + name), exist_ok=True)

        return self.get_cwd('/' + name)

    def create_image_folder(self):
        """Creates a folder to store the images into."""
        name = input("Name your images destination folder.")
        if name == '':
            name = 'Images'

        if os.path.isdir(self.get_cwd("/" + name)) is False:
            os.makedirs(self.get_cwd('/' + name), exist_ok=True)

        return self.get_cwd('/' + name)

    def create_data_file(self):
        """Creates the file that will keep track of the downloaded images
        and prevent them to be downloaded twice."""
        name = input("""Name your data file.""")
        if name == '':
            name = 'Data'

        if os.path.isfile(self.get_cwd(name)) is False:
            os.mknod(name + '.txt')

        return self.get_cwd('/' + name + '.txt')

    def create_list_data(self):
        """Creates the list data file, where the user is supposed to add,
        one per line, the link of the websites he wants to download images
        from."""
        name = input("Name of your websites list.")
        if name == '':
            name = 'Websites List'

        if os.path.isfile(self.get_cwd('/' + name)) is False:
            os.mknod(name + '.txt')

        return self.get_cwd('/' + name + '.txt')


class DataManager:
    """The DataManager class works with an Environment class' instance.
    It manages the information by returning it when requested, while also
    storing the program's data on the data file precissed."""

    def __init__(self, environment):
        self.this_environment = environment

    def return_env_dir(self):
        """Getter method for the environment folder of this     environment."""
        return self.this_environment.env_folder

    def return_images_dir(self):
        """Getter method for the images folder of this environment."""
        return self.this_environment.image_folder

    def return_data_file(self):
        """Getter method for the data file of this environment."""
        return self.this_environment.data

    def return_list_data(self):
        """Getter method for the list file of this environment."""
        return self.this_environment.list_data

    def save_pages_in_data(self, pages):
        """Saves the downloaded images into the data file. The downloaded images
        are a list of strings."""

        with open(self.datafile, 'a') as data:
            json.dump(pages, data, ensure_ascii=False)

    def get_pages_list(self):
        """Reads the websites stored on listdata.txt to tell the program where
        to look and download from."""

        with open(self.list, 'r') as pages:
            return pages.readlines()

    environment = property(return_env_dir)
    folder = property(return_images_dir)
    datafile = property(return_data_file)
    list = property(return_list_data)

### SINGLETON ###


def download_image(url, request_response):
    """Downloads an image from a given request. It names it the same as the
    requested url and saves it into the Puppies folder.

    The folder name in open(os.path.join(foldername)) etc. must be the same
    folder name stablished on the create_folder() function of setup.py """

    filename = url.split('/')[-1]
    with open(os.path.join(DATAMANAGER.folder, filename), 'wb') as image:
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

    pages = DATAMANAGER.get_pages_list()
    alr_dow = []

    for x in range(0, 1):

        look_images(pages, alr_dow)
        DATAMANAGER.save_pages_in_data(alr_dow)


if os.path.isdir(EnvironmentSetup.get_cwd('/Environment')) is False:
    THIS = EnvironmentSetup()
    DATAMANAGER = DataManager(THIS)
    with open('env_pickle', 'wb') as f:
        pickle.dump(THIS, f)
else:
    with open('env_pickle', 'rb') as f:
        THIS = pickle.load(f)

DATAMANAGER = DataManager(THIS)
get_page()

