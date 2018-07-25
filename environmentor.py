#! /usr/bin/python3

"""This script creates a new environment with all its elements."""

import os
import pickle
import shutil

from lib.envsetup import EnvironmentSetup
from lib.datamanager import DataManager


def clear_all_data(env_data):
    """Clears all data returning the environment system
    to a new-born stage, as if no environment was ever created."""

    with open("environmentor_data", "wb") as pickle_env_data:
        for data in env_data:
            shutil.rmtree(data.environment)
        env_data.clear()
        pickle.dump(env_data, pickle_env_data)


def clear_environment_data(env_data):
    """Clears all data from a specific environment."""

    if len(env_data) <= 0:
        print("There are no environments settled in here!")
        return
    with open("environmentor_data", "wb") as pickle_env_data:
        counter = 0
        print("Existing environments:")
        for data in env_data:
            print(str(counter), ": ", data.environment)
            counter += 1
        action = input("""Type the index number of the environment you want
        to erase""")
        try:
            shutil.rmtree(env_data[int(action)].environment)
            del env_data[int(action)]
            pickle.dump(env_data, pickle_env_data)
        except (ValueError, IndexError):
            print("No valid value was introduced.")
            pickle_env_data.close()


def create_environment(env_data):
    """Creates an environment and communicates of its creation to the
    environmentor_data file."""

    with open("environmentor_data", "wb") as pickle_env_data:
        environment = EnvironmentSetup()
        datamng = DataManager(environment)
        env_data.append(datamng)
        pickle.dump(env_data, pickle_env_data)

        print("\nEnvironment succesfully created.")


def create_environmentor_data(env_data):
    """Creates the environmentor_data file, which keeps a register of the user's
    current environments."""

    if os.path.isfile(EnvironmentSetup.get_cwd("/environmentor_data")) is False:
        with open("environmentor_data", "wb") as pickle_env_data:
            pickle.dump(env_data, pickle_env_data)


def environmentor_data_sort():
    """Gets the environmentor's data from the environmentor's data file, which
    is created firstly if it doesn't exist."""

    try:
        with open("environmentor_data", "rb") as pickle_env_data:
            env_data = pickle.load(pickle_env_data)
            print("it exists")
            return env_data
    except FileNotFoundError:   # If EOFError is added as exception, the error
                                # is masked but is not solved. Result: new env
                                # data created on each run.
        print("Creating data")
        env_data = []
        create_environmentor_data(env_data)
        return env_data


def environmentor():
    """Joins all the methods together. Gets the environmentor's data through
    the environmentor_data_sort() function and offers the user three possible
    actions: to create an environment, to clean a specific environment's data
    or to clean all the environmentor's data and leave everything as new."""

    env_data = environmentor_data_sort()
    action = input("""Press n to create new environment; s to erase an environment
    and c to erase all environments.""")
    if action == "n":
        create_environment(env_data)
    elif action == "c":
        action = input("""Are you sure? This will erase all of your environments
        and their data permanently! y/n""")
        if action == "y":
            clear_all_data(env_data)
        elif action == "n":
            environmentor()
    elif action == "s":
        clear_environment_data(env_data)


environmentor()
