#! /usr/bin/python3

"""This script creates a new environment with all its elements."""

import os
import pickle

from lib import datamanager, envsetup

if os.path.isfile(envsetup.EnvironmentSetup.get_cwd("/environmentor_data")) is False:
    ENV_DATA = []
    with open("environmentor_data", "wb") as f:
        pickle.dump(ENV_DATA, f)
else:
    with open("environmentor_data", "wb") as f:
        print(str(ENV_DATA))
        ACTION = input(
            "Press n to create a new environment; c to clean environments")
        if ACTION == 'c':
            ENV_DATA.clear()
            pickle.dump(ENV_DATA, f)
        elif ACTION == 'n':
            ENVIRONMENT = envsetup.EnvironmentSetup()
            DATAMANAGER = datamanager.DataManager(ENVIRONMENT)
            ENV_DATA.append(DATAMANAGER)
            print("Current environments: \n")
            pickle.dump(ENV_DATA, f)

with open("environmentor_data", "rb") as f:
    CONTENT = pickle.load(f)
    print(str(CONTENT))
