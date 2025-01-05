# setup/
## Python Install
Install [python 3.12](https://www.python.org/downloads/)

Troubleshooting:
- ensure the `path` is set correctly, do some googling if you get an error like `command not recognized`

## Virtual Enviornment Setup
The virtual enviornment must be set up at the root of this repository. It will automatically be gitignored, but it must be created using **requirements.txt** for the dependencies. 

You can either run the automated script **venv_help_windows.bat** after navigating to the root of this repository in command prompt, or [follow this guide](https://docs.python.org/3/library/venv.html).

Note that every time you run any python script here you will need to do it from the venv using `venv\Scripts\activate` at the root of this repo, unless it is already activated, in which case you will see `(venv)` at the left of your command prompt.

