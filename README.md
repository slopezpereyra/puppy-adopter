# PuppyAdopter
A program that downloads images of puppies and other baby animals.


# Puppy Adopter!

--- What is it? ---

PuppyAdopter matters because of its form and not of its content. It is essentially a program that scraps a list of web pages and downloads one picture, randomly selected, of each. The fact that it downloads pictures is incidental; since it was made to work as a structure, it only provides me the skeleton to later on build more complex, interesting programs, that download better -yet surely less cute- things than puppies and other baby animals.

# --- Where does it need to improve? --- 

PuppyAdopter does things that I would like to prevent from happening in the future. Here are the things I need advise on:

# Downloading unwanted images:

PuppyAdopter counts how many web objects with the 'img' or 'src' tags exist in a web page and chooses randomly one to download. The problem is, of the hundred or fifty images that the web page holds, some are unwanted, such as calendars, logos, publicity, and so. Not puppies. You get the idea. I haven't figure out a filter that works completely propperly, though have some things in mind and ran some tests. This is still unresolved.

# Ilegible data file:

This is a matter of ignorance from my part. PuppyAdopter produces a data file and stores in it, under the key "saves", a list value containing the url's of the downloaded images. Theoretically this, that was done for the purpose of preventing downloading twice the same file, works, since if one prints the list as a debug test the values are okay, and the function that saves the list has any issue to my mortal, beginner eyes. But, when the data file is opened (it is a .dat file) everything is ilegible, and I'd think my list should be there and not those strange characters. This could be: a) the list is not saved propperly on the .dat file and instead crazy characters are holded for some reason; b) the list is stored propperly but the .dat file is not legible because of its format. So... is it that the format can't be read on Word/NotePad/others or rather a fault on the program?

# The pages list:

The fact that the program works with a given list of web sites is limiting. On the other hand, it would be quite a mess to have the program scrap the whole web looking for puppies, even
with the propper filters. It would be much slower and vulnerable to bugs and unwanted results (such as downloading things that aren't puppies). Is there a way to find a solution
to this, apart from adding to the pages list a higher amount of values (web sites)?

# The os directory [Solved]:

--- The first defined function of the script solved this issue ---

# --- What do I want to achieve with PuppyAdopter? ----

Nothing. It's a crappy program. It is a simple excercise on web scrapping and downloading stuff that will on the process make me look cute on the eyes of my girlfriend (oh, the secret reasons of our endeavours!). I will subsequently use my PuppyAdopter experiencie to achieve more honourable goals (?).
