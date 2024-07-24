# try OpenAI API

![A test image](image.png)

# Environment setup

- Install dependencies required for python:

`sudo apt-get update && sudo apt-get install build-essential sqlite3`

- Install pyenv:

`curl https://pyenv.run | bash`

- Update .bashrc:

`echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc`

`echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc`

- Set up OpenAI token:

`echo -e 'export OPEN_API_TOKEN="YOUR OPEN API TOKEN"' >> ~/.bashrc`

- Refresh shell:

`exec "$SHELL"`

- Install dependencies:

`./scripts/install_dependencies.sh`

- Execute:

`python ./src/helloworld.py "Your query"`

# [Open AI pricing](https://openai.com/api/pricing/)