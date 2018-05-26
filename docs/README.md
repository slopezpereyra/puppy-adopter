
# Puppy Adopter*

Who doesn't love puppies?

# -- What is it? --

A few branches back I wrote PuppyAdopter was nothing more than a program that downloaded images. Now I can say its something -a little bit something- more. Its name comes from those previous versions -which are still public on this repository- in which it downloaded only puppies' images from a predetermined web-sites list. Now PuppyAdopter works through a web-sites list each user gives, containing of course whatever type of images, what results in a customizable download system. You could add web-sites holding images of landscapes, animals, philosophers, writers, cars or pretty much anything else, to download images from.

PuppyAdopter handles information smartly now; it does not download the same image twice and its data sytem is a very safe and comfortable way to handle user-given information and create a customized web-sites list.

# -- How does it work? --

PuppyAdopter creates a decent working enviroment to download your images and manage all the information it gets. When you first run PuppyAdopter.py, you'll be requested to name your images folder (where your images will be stored), a data file and a list data file. You can name them whatever you want. It will also create an Environment folder, which you must always leave there, and a pickle data file.

The great thing about it is that you can set as many enviroments as you want. You can place PuppyAdopter on a folder named Writers, execute it there and set an environment. Then you could do the same on a folder named Scientists. At last, you could tell PuppyAdopter to gather writers images on one environment, and scientists images on the other. You can have as many environments as you want!

PuppyAdopter downloads images from a websites list you provide to him on each environment. To do so is simple: simply paste as many links as you like on your list file (however you named it when the environment was setted), one link per line (that is important!). Once your list file has websites on it, if you run PuppyAdopter again, instead of creating an environment it will pass unto filling yours with images from the websites you provided. Beautiful!

# -- Instructions --

1 ) SET AN ENVIRONMENT

1.1 Place the PuppyAdopter.py file on any folder you want. Name the folder whatever you want.

1.2 Run PuppyAdopter.py. You'll be requested to name a folder, a data file and a list file. Do so.

2 ) PROVIDE YOUR WEBSITES

2.1 Once you named your files and folder and your environment is setted, paste on your list file the links of the pages you want PuppyAdopter to download images from to this environment. You can place as many links as you want, though the more you add the longer it will take for the program to run. (Remember to add only one link per line, this is important!)

3 ) ADOPT SOME PUPPIES!

3.1 Once your list file is filled with the websites you'd like to download images from, run PuppyAdopter.py again and see your images folder get filled with images! Beautiful...


Remember you can add as many websites as you like to your environments. Each environment must have its own copy of PuppyAdopter.py on its directory; each copy will handle only one environment.

# -- KNOWN BUGS --

 - PuppyAdopter runs, but doesn't download anything!

  Check that you've actually provided your list file (which you create when creating an environment) with links (see step 2 of instructions). Remember that's where PuppyAdopter gets directions! If you don't tell him where to go on your lists file, he'll go nowhere!
  This can also be caused by the pressence of a link in your list file that takes to a website that requests captcha or displays adds and pop-ups. You can not download from such websites with this program.

- PuppyAdopter downloads unwanted images

The biggest inconvinience of this program is its lack of artificial intelligence at the time of choosing a random image to download from a web-site. Among the hundred of pictures of, let's say, landscapes an X website holds, there might be a few not precisely desired: logos, advertisements or simply an undercover monster-truck photograph no landscapes lover would want. The program does not know how to distinguish them; if in the random selection the chance falls on the monster-truck, or the logo, or any other undesired image, the program will download it anyway.

This problem can be solved through machine learning. This is something I plan to learn and apply to the program. But, as you may see if check how much time there's between each edition of this repository, I don't have the time I need to do so now, since I am learning other computer languages and studying... well, things not related to Python or machine learning.
