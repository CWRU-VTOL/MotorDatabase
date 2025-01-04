# scripts
## Overview
### Note: This repository is transitioning to the **utility** folder with more generalized and structured utilities to replace this scripts folder and its contents.

This folder contains scripts that are intended to help in acquiring and processing the UAV motor data into the standardized format we made here.

Each script will have documentation, and its location (tentatively) will be inside the folder in which it is located. 

# Usage
Note that the python virtual enviornment must be set up as detailed in the repository wide README for these scripts to work.

## Organization
The scripts are organized as such:
```plaintext
scripts/
├── data_acquisition/
│   ├── brand_specific/
│   │   ├── ...
│   ├── generic_tools/
│   │   ├── ...
├── data_processing/
│   ├── brand_specific/
│   │   ├── ...
│   ├── generic_tools/
│   │   ├──process_preliminary_csv.py
│   │   ├──
│   │   ├── ...
└── README.md
```

**data_acquisition** contains tools for acquiring the data and converting it into the standardized format, and has tools that are both brand specific and generic.

**data_processing** contains tools for processing data which is in the standardized csv format, such as performing common calculations and formatting tasks.

**process_preliminary_csv.py** is designed to take a roughly formatted document in which the columns mostly adhere to the parameter format and return a strictly formatted version in which the parameters included and 