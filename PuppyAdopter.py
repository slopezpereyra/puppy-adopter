#! /usr/bin/python3

import os, requests, bs4, random, shutil, sys, json

# Major changes submited: no more shutil module to handle data storing; now shutil only handles downloading.
# Data storing is now managed partially by json module's methods, apart from regular reading and writing functions.
# In order to preserve added web sites, the added urls are not directly appended to the pages list, but stored in 
# a .txt file from which the pages list later gets its values.

# (This actually creates a pseudo-permanent list. The pages list is modified in the program, then saved in the .txt file.
# When the program is closed, the changes made to the list are lost; the list is reseted each time. But each time it runs, it
# also loads the values stored on .txt. So actually the list is always reseted to default, and only
# "remembered" through reading the values on the .txt file. The list is, but isn't, permanent.)

# Also removed the long menu. Unnecessary.
# Several optimization changes.

# The use of global variables is not recommended. Nevertheless, the declaration of pages as a global 
# makes everything easier, since it's constantly accesed and changed by other scripts.
# Its use was carefully thought. Af all variables, it is the only global.

# PROBLEMSwhen the pages list appends the value not from the program but from the
# listdata file, it appends it as a string. The list the is: ["a"], ["b"]... ["'x'"]. The program then scraps the
# web with an url delimited by quotation marks. Of course, this produces an error. 
# The most obvious methods were tried (strip, replace, etc.) and none of them worked correctly.

# --- PUPPYADOPTER_SCRIPT --- #

# Global Variable declaration #

pages = ['https://pixabay.com/es/photos/puppy/',
    'https://www.petsworld.in/blog/cute-pictures-of-puppies-and-kittens-together.html',
    'https://pixabay.com/es/photos/bear%20cubs/',
    'https://pixabay.com/es/photos/?q=cute+little+animals&hp=&image_type=photo&order=popular&cat=',
    'https://pixabay.com/es/photos/?q=baby+cows&hp=&image_type=photo&order=popular&cat=',
    'https://www.boredpanda.com/cute-baby-animals/']

# Preparatory (basic) definitions #

def get_cwd(appended_value):
    cwd = os.getcwd()
    cwd = cwd + appended_value

    return cwd

def create_folder():
    os.makedirs('Puppies', exist_ok=True)

# Data storing definitions #

def create_data_file():
    if os.path.isfile(get_cwd('/data.txt')) == False:
        os.mknod("data.txt")

def save_pages_in_data(saves_list):
    with open('data.txt', 'a') as outfile:
        json.dump(saves_list, outfile, ensure_ascii=False)

# List manipulation definitions #

def create_list_data():

    if os.path.isfile(get_cwd('/listdata.txt')) == False:
         os.mknod("listdata.txt")

def get_list_from_data():

    if user_appended == True:
        list_path = get_cwd('/listdata.txt')

        with open(list_path, 'r') as outfile:
            lecture = outfile.read()
            pages.append(lecture)
            for i in pages:
                i.replace('"', '')
            print(pages)

def manipulate_pages_list():

    user_appended == False

    answer = input('Press y to add new pages. Something else to start.')
    if answer == "y":
        while True:
            appended_link = input('Please, copy the links here. Type "f" to finish.')
            if appended_link == "f":
                break
            with open('listdata.txt', 'a') as outfile:
                user_appended == True
                json.dump(appended_link, outfile, ensure_ascii=False)

    if user_appended == True:
        get_list_from_data()

# Scraping  and downloading definitions #

def download_image(url, request_response):
    local_filename = url.split('/')[-1]
    with open(os.path.join('Puppies', local_filename), 'wb') as f:
        shutil.copyfileobj(request_response.raw, f, [False])

def get_random_url(web_object, web_object_number):

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
                    print("¿No fue adoptado ya este cachorrito? Reanudando...")
                    continue
                else:
                    return url_variable
                    break
        except IndexError:
            print('Algo salió mal: reanundando búsqueda...')
            continue

def look_images(pages_list, saves_list):

    for i in pages_list:
        print(i)
        res = requests.get(i)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        object = soup.select('img')
        object_number = len(object)

        print("\n Se encontraron {} cachorritos potenciales...".format(int(object_number)))
        print("\n Evaluando colmillitos y patitas...")
        image_url = get_random_url(object, object_number)
        print("\n Se encontraron vauitos...")
        print("\n Adoptando cachorrito...")

        if str(image_url).endswith('.jpg 2x'):
            image_url = str(image_url.replace(' ', '')[:-2])
        if not str(image_url).startswith("http"):
            image_url = "https://" + str(image_url)
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        saves_list.append(str(image_url))
        download_image(image_url, response)
        print('¡Cachorrito adoptado!')
        
def get_page():

    alr_dow = []


    create_folder()
    create_data_file()
    create_list_data()
    manipulate_pages_list()
    get_list_from_data()
    look_images(pages, alr_dow)
    save_pages_in_data(alr_dow)

get_page()

