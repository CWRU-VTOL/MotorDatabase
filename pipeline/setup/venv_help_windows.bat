@echo off
echo Setting up the virtual environment...

REM Create venv
py -3.12 -m venv venv

REM Activate venv
call venv\Scripts\activate

REM Install dependencies
pip install -r requirements.txt

echo Virtual environment setup complete!
pause