# KDE
## Overview
This folder contains scripts used to automatically acquire data for KDE motors. 

## Contents
Currently, **acquire_raw_data.py** will be run from the VENV and depending on how its main() function is configured it will pull all/specific parts of the motor data. 

## Compatibility
I'm pretty sure the file paths and some light hardcoding means that this script currently only works with windows, and requires running the program with the KDE folder as the working directory.

## Organization
There are 3 folders of data, and the file naming follows the naming convention established. In **motor_specs** there are specicifications for each motor. In **performance_specs** there are performance specifications with many datapoints for the specific performance of the motor under specific conditions. In **temp** there is currently the **gridData.csv** which is the URL links, names, and prices of each of the motors pulled from the grid of motors.