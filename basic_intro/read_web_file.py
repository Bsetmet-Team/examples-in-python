#! /usr/bin/python3
# Make scripts independant with this method or create a package...
# https://stackoverflow.com/a/44210735/1146659
import sys
import subprocess
import pkg_resources
import os
import time

required = {
        "numpy",
        "pandas",
}


installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# wait until modules are installed
time_to_wait = 60
time_counter = 0
#while not os.path.exists(file_path):
while len(required-installed) != 0
    time.sleep(1)
    time_counter += 1
    if time_counter > time_to_wait:break

print("done")

import pandas as pd
data = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print(data)
