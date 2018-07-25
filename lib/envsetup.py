import os
import pickle
import sys


class EnvironmentSetup:

    """Creates the basic folders and files an environment will manage data on.
    An environment is simply a place in your system in which, and with which
    elements, PuppyAdopter will operate. You can have as many environments
    as you want: "Writers", for instance, may be dedicated to downloading writers
    pictures; "Puppies",puppies pictures, and so."""

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

        name = input("Name this environment: ")

        if os.path.isdir(self.get_cwd("/" + name)) is False:
            os.makedirs(self.get_cwd('/' + name), exist_ok=True)
        else:
            print("This environment already exists!")
            sys.exit(0)

        return self.get_cwd('/' + name)

    def create_image_folder(self):
        """Creates a folder to store the images into."""

        name = input("Name your images destination folder: ")
        if name == '':
            name = 'Images'

        if os.path.isdir(self.env_folder + "/" + name) is False:
            os.makedirs((self.env_folder + "/" + name), exist_ok=True)

        return self.env_folder + "/" + name

    def create_data_file(self):
        """Creates the file that will keep track of the downloaded images
        and prevent them to be downloaded twice."""

        name = input("""Name your data file: """)

        if name == '':
            name = 'env_data'

        if os.path.isfile(self.env_folder + "/" + name) is False:
            os.mknod(self.env_folder + "/" + name + ".txt")

        return self.env_folder + "/" + name + ".txt"

    def create_list_data(self):
        """Creates the list data file, where the user is supposed to add,
        one per line, the link of the websites he wants to download images
        from."""

        name = input("Name of your websites list: ")

        if name == '':
            name = 'websites_list'

        if os.path.isfile(self.get_cwd(self.env_folder + "/" + name)) is False:
            os.mknod(self.env_folder + "/" + name + '.txt')

        return self.env_folder + "/" + name + '.txt'
