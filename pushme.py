import os
import sys
import subprocess

os.chdir("/data/Prog/PyCharm/")

what = sys.argv[1].lower()

for dirnm in os.listdir("."):
    if dirnm.lower() == what:
        what = dirnm
        break

os.chdir(what)
subprocess.call("git pull", shell=True)
subprocess.call("git commit -am AutoCommit", shell=True)
subprocess.call("git push", shell=True)

print("Köszönöm a segítséget Husi Pipi!")
