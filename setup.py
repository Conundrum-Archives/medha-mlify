import sys
import shutil
import setuptools
from pathlib import Path

'''
    This file builds the library for pypi. To run the setup, execute the command:
    python setup.py sdist bdist_wheel --buildversion <version-num>
'''

def cleanPrevBuild():
    '''Clears the previous build data, if any.'''
    cleandirs = ["dist", "mlify.egg-info"]
    for dir in cleandirs:
        dirpath = Path(dir)
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)


def readReadmeFile():
    '''readReadmeFile def will read readmefile and return the content ans string. used for filling library readme.'''
    with open(configurations["readmefile"], "r") as rf:
        return str(rf.read())

def startSetup(configurations):
    '''startSetup def will start the build/setup of py project'''
    setuptools.setup(
      name = configurations["projectname"],
      version = configurations["libraryversion"],
      author = configurations["author"],
      author_email = configurations["authoremail"],
      packages = setuptools.find_packages(where="src"),
      package_dir = {
        "": "src"
      },
      data_files = [
        ('', [
            # add files to add to dist
        ])
      ],
      include_package_data = True,
      description = configurations["projectdescription"],
      long_description = readReadmeFile(),
      license = configurations["license"],
      python_requires = configurations["pythonrequires"],
      install_requires = [
            # add library dependencies with version
      ],
      setup_requires = [
        "wheel",
        "pytest-runner"
      ],
      tests_require = [
        "pytest==4.4.1"
      ],
      classifiers=configurations["classifiers"],
    )

if __name__  == "__main__":

    configurations = {
        "projectname": "mlify",
        "license": "GPL-3.0",
        "authoremail": "medha@conundrum.org",
        "author": "@Conundrum-Archives/Medha-Team",
        "libraryversion": "0.0.0",
        "projectdescription": "A ML LAB library for ML application in conundrum team",
        "readmefile": "README.md",
        "pythonrequires": ">=3.6",
        "classifiers": [
            "Development Status :: 1 - Milestone",
            "Topic :: ML",
            "License :: OSI Approved :: GPL-3.0-or-later",
        ]
    }

    # call clean definition to clear prev build data
    cleanPrevBuild()

    # check if version is passed during build of setup.py
    if "--buildversion" not in sys.argv:
      raise("provide build version with --buildversion <version.number> parameter")

    # get version value from cli-arguments
    index = sys.argv.index('--buildversion')
    sys.argv.pop(index)
    configurations["libraryversion"] = sys.argv.pop(index)

    # start setup
    startSetup(configurations)
