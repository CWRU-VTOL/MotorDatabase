# scripts
## Overview
This folder contains scripts that are intended to help in acquiring and processing the UAV motor data into the standardized format we made here.

Each script will have documentation, and its location (tentatively) will be inside the folder in which it is located. 

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
└── README.md
```

**data_acquisition** contains tools for acquiring the data and converting it into the standardized format, and has tools that are both brand specific and generic.

**data_processing** contains tools for processing data which is in the standardized csv format, such as performing common calculations and formatting tasks.