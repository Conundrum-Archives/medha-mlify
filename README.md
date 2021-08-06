![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mlify)  ![PyPI](https://img.shields.io/pypi/v/mlify)

![GitHub Repo stars](https://img.shields.io/github/stars/conundrum-archives/medha-mlify?style=social) ![GitHub contributors](https://img.shields.io/github/contributors/conundrum-archives/medha-mlify?style=social)

![PyPI - License](https://img.shields.io/pypi/l/mlify)




# Medha - MLIFY
## This repo is a codebase for ML functionality and libraries for Medha-Rover.

Medha-Rover is a rocker-bogie rover inspired by Nasa's Curiosity rover.
Medha is set to function and test phase of prototype-1 under test-lab environment in progress.

## Supported and managed by Conundrum-Archives
Conundrum-Archives is an initiative and network of enthusiasts who work and contribute on space, science, technology and sustainability. Everything in Conundrum-Archives is driven by curiosity.
Follow Conundrum-Archives [Instagram](https://www.instagram.com/conundrum_archives/) and [Podcast](https://open.spotify.com/show/5nzZu8kbqktq22U3GpRYGP) for more updates.
> keep the conundrum rolling

for any concerns and support, please reach out to **@medha-team** or **@conundrum-archives-team**.

## Tech

Medha-MLIFY is started as open-source project and remain open-source forever.

## Installation

Pre-req:

- [Python 3.6.x +](https://www.python.org/downloads/)
- Python libraries
- [git](https://git-scm.com/downloads) (required for working with repo)
- good to have ML libraries (eg. numpy, opencv-python, etc)

For cloning this repo...

```sh
git clone https://github.com/Conundrum-Archives/medha-mlify.git
```

to change branch / milestone:
```sh
cd medha-mlify
git checkout -b <branch-name>
git pull origin <branch-name>
```

Note: It is good to work under virtual environment. to setup virtual environment, make sure venv library is installed.
```sh
python -m venv venv

# for windows cmd-prompt
venv\Scripts\activate

# for linux-terminal
$ source venv/bin/activate
```

#### Building for source

```sh
python setup.py sdist bdist_wheel --buildversion <version-num>
```

## License
GPL-3.0
