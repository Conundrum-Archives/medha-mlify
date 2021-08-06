import sys
import shutil
import setuptools
from pathlib import Path

'''
    This file builds the library for pypi. To run the setup, execute the command:
    python setup.py sdist bdist_wheel --buildversion <version-num>
'''

def clean_prevbuild():
    '''Clears the previous build data, if any.'''
    cleandirs = ["dist", "mlify.egg-info"]
    for dir in cleandirs:
        dirpath = Path(dir)
        if dirpath.exists() and dirpath.is_dir():
            shutil.rmtree(dirpath)


def read_readmefile():
    '''readReadmeFile def will read readmefile and return the content ans string. used for filling library readme.'''
    with open(configurations["readmefile"], "r") as rf:
        return str(rf.read())

def start_setup(configurations):
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
      long_description = read_readmefile(),
      long_description_content_type="text/markdown",
      license = configurations["license"],
      python_requires = configurations["pythonrequires"],
      test_suite = configurations["test_suite"],
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
        "license": "GNU General Public License v3 or later (GPLv3+)",
        "authoremail": "podcast.conundrum@gmail.com",
        "author": "@Conundrum-Archives/Medha-Team",
        "libraryversion": "0.0.0",
        "projectdescription": "A ML LAB library for ML application in conundrum team",
        "readmefile": "README.md",
        "pythonrequires": ">=3.6",
        "test_suite": "tests",
        "classifiers": [
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9"
        ]
    }

    # call clean definition to clear prev build data
    clean_prevbuild()

    # check if version is passed during build of setup.py
    if "--buildversion" not in sys.argv:
      raise Exception("provide build version with --buildversion <version.number> parameter")

    # get version value from cli-arguments
    index = sys.argv.index('--buildversion')
    sys.argv.pop(index)
    configurations["libraryversion"] = sys.argv.pop(index)

    # start setup
    start_setup(configurations)
