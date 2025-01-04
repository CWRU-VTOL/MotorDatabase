# MotorDatabase
## Overview and Purpose
Welcome to **MotorDatabase** — CWRU VTOL's repository dedicated to establishing a **standardized .csv format** for UAV motor performance data and specifications. 

## Features
- **Standardized Format**:
  - Ensures consistency across all motor data, following [formatGuidelines.md](reference/formatGuidelines.md).
  - Handles missing parameters gracefully.
- **Automation-Friendly**:
  - Easily integrates with data analysis pipelines.
- **Human-Readable**:
  - Clear organization for quick manual inspection.
- **Utilities for Varied Inputs**
  - provides tools for processing, acquiring, organizing, formatting, and visualizing motor data from highly varied sources.
- **Extensible**:
  - Allows inclusion of additional parameters and notes as needed.

## Usage
The main usage of the repository is as follows:
- Referencing/using the standardized motor data csv files.
- Using scripts or utilities from this repository for tasks related to those standardized motor data csvs.

It is recommended to read [formatGuidelines.md](reference/formatGuidelines.md) and [namingGuidelines.md](reference/namingGuidelines.md) to understand how the data is structured.

The **scripts** and **utility** folders have README's that provide further details on their usage.
## Structure 
The repository is structured as follows:

```
MotorDatabase/
├── csv/
├── reference/
│   ├── formatGuidelines.md
│   ├── namingGuidelines.md
│   ├── template.csv
│   └── template_simplified.csv
├── scripts/
├── utility/
├── requirements.txt
├── LICENSE
└── README.md
```
## Contents
- **csv/**
  - Contains motor data in the standardized csv format specified by this repository.
  - Organized into subfolders based on brand.
- **reference/**
  - Documentation and templates for standardizing motor data.
  - Includes:
    - `formatGuidelines.md`: Rules for formatting.
    - `namingGuidelines.md`: Naming conventions.
    - `template.csv`: Example of a fully populated CSV.
    - `template_simplified.csv`: Simplified template.
- **scripts/**
  - Miscellaneous scripts, tools, and some raw extracted data.
- **utility/**
  - Contains the main utitilites and programs for acquiring, processing, cleaning, displaying, and exporting motor data. 
  - Currently a work in progress, ideally will eventually have a GUI or at least a single streamlined main program.  
- `requirements.txt`
  - Lists Python dependencies for the project.
- `LICENSE`
  - The license for the repository.
- `README.md`
  - Main documentation for the project.

## Requirements and Setup
The main requirements to this project are python based, and use a virtual python environment to reliably manage dependencies. 

Please ensure that **Python 3.12** is installed and then create a **venv** at the root of this repository using **requirements.txt**.

If you are on Windows you can use **utility\venv_help_windows.bat** to automatically set up the venv, assuming python 3.12 is installed. 

*Note that as of 1/4/25 certain scripts or utilities may reference file paths in a windows-specific way, and Linux or Mac compatibility is currently untested for these components.*
*Further documentation and resources for python setup help may be added in the future if needed.*

---

## Contributing
Currently this project is under work by CWRU VTOL but it will likely be open to community contributions in the future, at which point contribution guidelines will be added. 

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments 
- (todo: as features implemented, be sure to update)

