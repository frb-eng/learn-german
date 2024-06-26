#!/bin/sh

# Required for python
# sudo apt-get install build-essential

project=learn-german
python_version=3.12.3

brew update && brew install pyenv pyenv-virtualenv

if ! pyenv virtualenvs | grep -q "$project"; then
    pyenv install $python_version
    pyenv virtualenv $python_version $project
    pyenv local $project
fi

pyenv activate $project

pip install -r requirements.txt