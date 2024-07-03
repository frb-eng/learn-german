#!/bin/sh

# Required for python
# sudo apt-get update && sudo apt-get install build-essential sqlite3

# Install homebrew
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Make sure you have the following in .bashrc
# alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"

project=learn-german
python_version=3.12.3

brew update && brew install python-tk pyenv pyenv-virtualenv 

if ! pyenv virtualenvs | grep -q "$project"; then
    pyenv install $python_version
    pyenv virtualenv $python_version $project
    pyenv local $project
fi

pyenv activate $project

pip install -r requirements.txt