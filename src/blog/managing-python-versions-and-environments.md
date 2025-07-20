---
title: Managing Python versions and environments
date: 2024-04-07
---

Python is lovely to write and tricky to install.

As a beginner, every time I reinstalled Python, I would get into a bramble of environment variables, bash profile scripts, and Python helpers like pyenv, virtualenv, virtualenvwrapper, and pip. But eventually I figured out a way I like and that works well.

So here is my opinionated guide, mainly for myself, but maybe for other Ubuntu users as well.

## Leave the system Python but install pip with apt

Leave the system-installed version of Python (e.g. 3.11 on Ubuntu 24.04) alone. Just add Python installation helpers and pip using apt. This will let you command `python3` and `pip` outside virtual environments.

This was the install script that was working for me in early 2024:

```sh
sudo apt update
sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev \
libxmlsec1-dev libffi-dev liblzma-dev
sudo apt-get install python3-pip
```

## Install pyenv

Install pyenv, which is how to get a different version of Python for a specific project.

```sh
curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

This makes it straightforward to add another version of Python. Unlike the system Python version, this version will be managed by pyenv.

```sh
pyenv install 3.10
```

## Create a virtual environment

Each time you want to set up a virtual environment, use [venv](https://docs.python.org/3/library/venv.html), not virtualenv or virtualenvwrapper.

Here are the key steps:

1. Use pyenv to switch globally to the version of Python you want.
2. Create your environment using that Python version’s venv module.
3. Then set the global Python version back to the system version.

For example:

```sh
cd myproject                   # Get inside your project.
pyenv global 3.10              # Set global `python` to version 3.10.
python --version               # Check that it’s set properly.
python -m venv .venv           # `.venv` names the environment folder.
pyenv global system            # Reset the global `python` command.
python --version               # Check that it’s reset.
echo "/.venv/" >> .gitignore   # Add `.venv` to .gitignore
```

In this example I have used `.venv` as the name of the environment. This will create a folder within the project directory with that name.

I like this placement for virtual environments, because I just like to be able to check their presence easily. I can run `ls -al` and see `.venv` in the results. There are other approaches which place the environment folder elsewhere.

I prefer using a hidden folder like `.venv` over a normal one like `venv` to ensure `site-packages` do not get picked up in command-line search tools. Most of them respect `.gitignore` and omit `site-packages` from results, but I have found a few that go instead by the dot-notation for hidden files.

## Activate it

You can activate the environment manually.

```sh
source .venv/bin/activate
```

Or you can automatically activate it with an IDE tool.

I use the Python plugin of Zsh to automatically activate it and display the environment in the terminal when I `cd` into it.
