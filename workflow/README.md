# Workflow/
*Note: Work in progress.*

## Overview
This folder contains the main utilities and programs for acquiring, processing, cleaning, displaying, and exporting motor data.

This is currently a work in progress. Ideally, it will eventually have a GUI or at least a single streamlined main program.

Each python script should have detailed documentation in the docstring for its usage and functions.
## Process
Typical steps (may use together or in parts):
1. Acquire data:
    - Could use **batch_input.py** to input a batch of files and preprocess them to get them ready.
    - Could use **web_scraper.py** if the website permits.
2. Organize and clean data:
    - Can use **organizer.py** to organize inputted data into the standardized format and clean it.
    - Can also use it to further organize to fit the template precisely.
3. Perform calculations on data:
    - If needed, **calculations.py** can perform calculations on the data.
4. Display and summarize data:
    - Data can be displayed and summarized using **summarize.py**.
5. Streamline and automate:
    - This process can be streamlined and automatically managed using **workflow.py** (note: not currently implemented).
6. Other functions:
    - Validation can be performed at each step and utilizes **validation.py**.
    - **file_utils.py** provides utilities both used by each step and useful on their own for importing and exporting data.

## Contents and Structure
```
workflow/
├── setup/
│   ├── README.md
│   ├── venv_help_windows.bat
├── temp/
├── utility/
│   ├── file_utils.py
│   ├── validation.py
├── batch_input.py
├── calculations.py
├── organizer.py
├── README.md
├── summarize.py
├── web_scraper.py
├── workflow.py
```

*Note: considering switching to structure with utils for utilities useful across the process, preprocess for handling inputs and non-standardized data, and process for processing mostly standardized data.*
## Setup
Follow the **README.md** in the setup folder for help setting up the Python dependencies, including links to guides and troubleshooting steps.

## Usage and Examples
TODO: Detail example usage of individual scripts and overall workflow.

## Troubleshooting
TODO: Detail common issues with setting up the workflow and using the components, and detailed solutions and troubleshooting steps.

