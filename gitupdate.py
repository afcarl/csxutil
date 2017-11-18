#! /bin/python

from __future__ import print_function

import os
from subprocess import run as srun

print("-"*50)
print("Updating git repos...")
os.chdir(os.path.expanduser("~/Prog/PyCharm"))
with open("/dev/null", "w") as null:
    for dirnm in os.listdir("."):
        os.chdir(dirnm)
        print("Updating", dirnm)
        srun(["git", "pull"], stdout=null, stderr=null)
        os.chdir("..")

print("-"*50)
print("Updated all git repos!")
