#! /usr/bin/python3

#Please read the readme to understand what this is and what is expected from it.

import os, requests, bs4, random, shelve, shutil

def create_folder():
    print('Comprobando pelusitas y pulguitas...')
    os.makedirs('Puppies', exist_ok=True)

def download_image(url, request_response):
    local_filename = url.split('/')[-1]
    with open(os.path.join('Puppies', local_filename), 'wb') as f:
        shutil.copyfileobj(request_response.raw, f, [False])

    return local_filename

def create_data_file():

    if os.path.isfile('C:\\Users\\usuario\\Documents\\santi\\saves.dat') == False:
        page_files = shelve.open('saves')
        page_files.close()

def save_pages_in_data(saves_list):
        if os.path.isfile('C:\\Users\\usuario\\Documents\\santi\\saves.dat') == True:
            page_files = shelve.open('saves')
            page_files['saves'] = saves_list
            page_files.close()

def get_random_url(web_object, web_object_number):

    while True:
        try:
            random_number = random.randint(0, web_object_number)
            url_variable = web_object[random_number].get('src')
            if not '.jpg' in str(url_variable):
                continue
            elif os.path.isfile('home/santiago/Documentos/PuppyAdopter/saves.dat') == True:
                if str(url_variable) in open('saves.dat', encoding='Latin-1').read():
                    continue
            return url_variable
            break
        except IndexError:
            print('Algo salió mal: reanundando búsqueda...')
            continue

def look_images(pages_list, saves_list): #This is where the magic happens!!

    for i in pages_list:
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

    pages = ['https://pixabay.com/es/photos/puppy/',
    'https://www.petsworld.in/blog/cute-pictures-of-puppies-and-kittens-together.html',
    'https://pixabay.com/es/photos/bear%20cubs/',
    'https://pixabay.com/es/photos/?q=cute+little+animals&hp=&image_type=photo&order=popular&cat=',
    'https://pixabay.com/es/photos/?q=baby+cows&hp=&image_type=photo&order=popular&cat=',
    'https://www.boredpanda.com/cute-baby-animals/']

    alr_dow = []

    create_folder()
    create_data_file()
    look_images(pages, alr_dow)
    save_pages_in_data(alr_dow)

get_page()
