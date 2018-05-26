#! /usr/bin/python3

"""This script creates a new environment with all its elements."""

import os
import pickle

from datamanager import DataManager
from envsetup import EnvironmentSetup

if os.path.isfile(EnvironmentSetup.get_cwd("/environmentor_data")) is False:
    ENV_DATA = []
    with open("environmentor_data", "wb") as f:
        pickle.dump(ENV_DATA, f)
else:
    with open("environmentor_data", "wb") as f:
        print(str(ENV_DATA))
        action = input(
            "Press n to create a new environment; c to clean environments")
        if action is 'c':
            ENV_DATA.clear()
            pickle.dump(ENV_DATA, f)
        elif action is 'n':
            ENVIRONMENT = EnvironmentSetup()
            DATAMANAGER = DataManager(ENVIRONMENT)
            ENV_DATA.append(DATAMANAGER)
            print("Current environments: \n")
            pickle.dump(ENV_DATA, f)

with open("environmentor_data", "rb") as f:
    content = pickle.load(f)
    print(str(content))
