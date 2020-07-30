#! /usr/bin/python3
# ------------------------------------------------------                                                                                                                # Make scripts independant with this method ... or create a package...
# https://stackoverflow.com/a/44210735/1146659
required = {
        "numpy",
        "pandas",
}
import sys
import subprocess
import pkg_resources
import time

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

# begin installing all missing modules with pip
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

time_to_wait = 60
time_counter = 0
# wait until modules are installed
while len(required - installed)>0:
    installed = {pkg.key for pkg in pkg_resources.working_set}
    time.sleep(1)
    time_counter += 1
    if time_counter > time_to_wait:
        break
# ------------------------------------------------------
# begin script code
import pandas as pd
import numpy as np

data = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print(data)

np_data=np.array(data)
print(data)
