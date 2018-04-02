#! /usr/bin/python3

"""Creates the basic folders PuppyAdopter will manage data on. """

import os


# Preparatory (basic) definitions

def get_cwd(appended_value):
    """Return the directory formed by the join of the working directory
    plus an appended value. Not a big deal, but makes things easier."""

    cwd = os.getcwd()
    cwd = cwd + appended_value

    return cwd

def create_folder():
    """Creates a folder to store the images into."""

    os.makedirs(get_cwd('/NameYourImageFolder'), exist_ok=True)

# Data storing definitions

def create_data_file():
    """If there's no data file yet (the case should be if it is the
    first time you run the program), it creates it."""

    if os.path.isfile(get_cwd('/data.txt')) is False:
        os.mknod("data.txt")

def create_list_data():

    """Creates a list data file named listdata.txt. In it you should store
    the websites you'd like to download images from, each link in a different
    line."""

    if os.path.isfile(get_cwd('/listdata.txt')) is False:
        os.mknod("listdata.txt")


create_folder()
create_data_file()
create_list_data()
