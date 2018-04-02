
*Puppy Adopter*

PuppyAdopter is nothing more than a program that downloads images. Its name comes from previous versions -which are still public on this repository-, in which it downloaded only puppies' images from a predetermined web-sites list. Now PuppyAdopter works through a web-sites list each users gives, containing of course whatever type of images, which makes its downloads customizable: you could add web-sites holding images of landscapes, animals, philosophers, writers, cars or pretty much anything else, to download images from.

PuppyAdopter handles information smartly now; it does not download the same image twice and its listdata.txt is a very safe and comfortable way to handle user-given information and make the web-sites list subject of manipulation (which was done in previous versions, though not exactly flawlessly and in a quite uncomfortable way).

Its only inconvenient is its lack of artificial intelligence at the time of choosing a random image to download from a web-site. Among the hundred of pictures of, let's say, landscapes an X website holds, there might be a few not precisely desired: logos, advertisements or simply an undercover monster-truck photograph no landscapes lover would want. The program does not know how to distinguish them; if in the random selection the chance falls on the monster-truck, or the logo, or any other undesired image, the program will download it anyway.

This problem can be solved through machine learning. This is something I plan to learn and apply to the program. But, as you may see if check how much time there's between each edition of this repository, I don't have the time I need to do so now, since I am learning other computer languages and studying... well, things not related to Python or machine learning.

Apart from this issue, the program is now flawless.

*Instructions*

Run setup.py; it will shut down after creating a folder and two data files: data.txt and listdata.txt. This two data files will be created on the same folder the .py file is.
Add the links of the pages you want to download images from, as many as you like, on the listdata.txt file and save it. Make sure you add one link per line, such as
www.a.com
www.b.com
www.n.com
because it won't function properly otherwise. I recommend adding 5 websites as a minimum on the listdata.txt file. From there, the sky is the limit!

Once you've added your websites you can run the program smoothly. You can erase or add new pages whenever you want.
