
# Puppy Adopter

### Who doesn't love puppies?


## What is it?

_**A super cool image downloader.**_

Puppy Adopter is an image-downloader and gallery manager software that aims at
making it easy to have different and numerous galeries of images in our
computers.


## How does it work?

Puppy Adopter works by allowing you to create different environments or galeries
to store your images at. You are to provide each environment's websites_list file,
which they have by default, with the links of the websites you want this environment
to download images from. To create or erase environments we use the environmentor.py
file. To begin the downloading process, which will furnish your environments with
images downloaded from their corresponding websites, we use the puppy_adopter.py file.

You can have as many environments as you want, and you can provide each environment
with as many websites you like. The sky is the limit!


## Detailed instructions

### Managing our environments:

You can think of an environment as a galery. It's a place where to download
images from a list of websites you provide. Each environment is independent
from the others, and has its own list of websites. **environmentor.py**
is the program that _manages our environments_. With it we can create or erase
environments.

To create and furnish an environment, run **envionmentor.py**. You'll be prompted
to erase one or all environments or create one. Choose to create one and name the
files of your environment when requested to. Among the files you've named, there
was a websites_list, which is a simple .txt file. **One per line**, paste in this file the
links of the websites this environment will download images from.

Once your environment was created and you provided its websites_list with links, we can
say that your environment is settled. Now you can just run **puppy_adopter.py** and
watch as the magic happens!


###### Erasing a single environment

**environmentor** offers us to erase a single environment. When an environment
is erased, all its files, folders and data are erased permamently.

When we chose these option, a list of our environments will be displayed, each
with an index number besides it. Then we are to enter the index number of the environment
we wish to erase and that will be all. This action is permanent so be wise when using it.


###### Erasing all environments

When we run **environmentor** we can also choose to erase all of our environments.
This resets the program to a new-born state: all files, folders and data are
erased permanently. Use it carefully and wiselly.


### Puppy-Adopting Process

If all your environments were provided with websites, it's time to furnish them!
To do so, simple execute PuppyAdopter. It will automatically do the job for you.
Once it's done, your environments should be furnished with images downloaded from
the websites you provided to them into to your computer.


## Important considerations

* Always remember to add the websites in your websites_list file! Otherwise nothing
will be downloaded.

* Remember you can add as many websites as you like to your environments; the
more websites, the more images!

* If you manually erase an environment's folder or its elements, this doesn't prevent
PuppyAdopter from considering this environment still exists. The reason is that this
environment's data wasn't properly erased by the program. This will very likely produce
errors. To properly erase an environment, use **environmentor.py**.

* Don't provide your environment's websites_list with links of websites that
request captcha or other types of controls, and neither of websites that display
pop-ups when opened. PuppyAdopter does not know how to close pop-ups nor how
to pass an AI control. Keep it simple!
