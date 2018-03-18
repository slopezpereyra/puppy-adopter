#! /usr/bin/python3

import os, requests, bs4, random, shutil, json, sys

# Run the program the first time and it will shut down after creating a folder and two data files: data.txt and listdata.txt. 
# This two data files will be created on the same folder the .py file is.
# Add the links of the pages you want to download images from, as many as you like, on the listdata.txt file and save it.
# Make sure you add one link per line, such as 
# www.a.com
# www.b.com
# www.n.com
# It won't function properly otherwise. I recommend adding 5 websites as a minimum on the listdata.txt file. From there,
# the sky is the limit!

# Once you've added your websites you can run the program smoothly. You can erase or add new pages whenever you want.


# Preparatory (basic) definitions

def get_cwd(appended_value):
    cwd = os.getcwd()
    cwd = cwd + appended_value

    return cwd

def create_folder():
    os.makedirs('NameYourImageFolder', exist_ok=True)

# Data storing definitions

def create_data_file():
    if os.path.isfile(get_cwd('/data.txt')) == False:
        os.mknod("data.txt")

def save_pages_in_data(saves_list):
    with open('data.txt', 'a') as outfile:
        json.dump(saves_list, outfile, ensure_ascii=False)

# List manipulation definitions

def create_list_data():

    if os.path.isfile(get_cwd('/listdata.txt')) == False:
         os.mknod("listdata.txt")
         sys.exit(0)

def get_list_from_data():

    list_path = get_cwd('/listdata.txt')

    with open(list_path, 'r') as outfile:
        lecture = outfile.readlines()
        return lecture

# Scraping  and downloading definitions

def download_image(url, request_response):
    local_filename = url.split('/')[-1]
    with open(os.path.join('Puppies', local_filename), 'wb') as f:
        shutil.copyfileobj(request_response.raw, f, [False])

def get_random_url(web_object, web_object_number):

    error_counter = 0

    while True:
        try:
            random_number = random.randint(0, web_object_number)
            url_variable = web_object[random_number].get('src')
            if not '.jpg' in str(url_variable):
                continue
            with open('data.txt') as data:
                lecture = data.read()
                if str(url_variable) in lecture:
                    continue
                    print("Wasn't this image downloaded already...? Restarting...")
                else:
                    return url_variable
                    break
        except IndexError:
            if error_counter < 5:
                print('Oops! Something went wrong. Starting again...')
                error_counter = error_counter + 1
                continue
            else:
                print("False returned.")
                return False
                

def look_images(pages_list, saves_list):

    for i in pages_list:
        print(i)
        res = requests.get(i)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        object = soup.select('img')
        object_number = len(object)

        image_url = get_random_url(object, object_number)
        if image_url == False:
            continue
        print("\n Images found...")
        print("\n Beginning download...")

        if str(image_url).endswith('.jpg 2x'): # This rare statement solves a problem: some files were downloaded with
            # an extra " 2x" string on their format, corrupting the file.
            image_url = str(image_url.replace(' ', '')[:-2])
        if not str(image_url).startswith("http"): # More circumstantial error preventions...
            image_url = "https://" + str(image_url)
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        saves_list.append(str(image_url))
        download_image(image_url, response)
        print('Puppy adopted!')

def get_page():

    pages = get_list_from_data()
    alr_dow = [] #alr_dow stands for 'already downloaded'. This is part of the process of preventing an image being 
    # downloaded repeatedly.

    for x in range(0, 1): # You could not add a range at all, but to download a lot this is good. Give a wider range
        # to download more images.
        
        create_folder()
        create_data_file()
        create_list_data()
        look_images(pages, alr_dow)
        save_pages_in_data(alr_dow)

get_page()
