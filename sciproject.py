import os
import sys
import subprocess

from os.path import exists
from os.path import expanduser as eu

dataroot = "~/SciProjects/"
progroot = "~/Prog/SciProjects/"


def createproject(name):
    if not exists(dataroot):
        os.mkdir(dataroot)
    if exists(dataroot + f"Project_{name}"):
        print(f"Project {name} already exits!")
        return 1

    os.mkdir(eu(f"{dataroot}Project_{name}"))
    os.mkdir(eu(f"{progroot}{name}"))

    py = f'from os.path import expanduser as _eu\nprojectroot = _eu("{dataroot}Project_{name}")\n'
    with open(f"{progroot}{name}/__init__.py", "w") as handle:
        handle.write(py)

    print(f"Created SciProject: {name}")


def updateproj(name):
    try:
        os.chdir(eu(f"~/SciProjects/{name}"))
    except FileNotFoundError:
        print("No such project:", name)
        if input("Should I create it? y/N >") == "y":
            return createproject(name)
        return
    subprocess.run(["git", "pull"])


def main():
    arg = sys.argv[1:]


if __name__ == '__main__':
    main()
