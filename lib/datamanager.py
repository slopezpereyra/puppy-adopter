import json


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
