# File Naming Guidelines
## Overview
As detailed in formatGuidelines.md, the file name is constructed from the following parameters in this order:
1. motor name prefix
2. motor name
3. motor name suffix
4. date accessed

The file name is constructed by taking each parameter, formatting it properly, and combining them with dashes in between.

Guidelines on how to format each parameter properly are listed below, and all scripting and programs expect this naming convention.

## motor name prefix
This parameter depends on the brand and can take the following values. As we add data we will add more brands.
- **APD**: motors from Advanced_Power_Drives
- **DJI**: motors from DJI
- **EMAX**: motors from EMAX
- **Hobbywing**: motors from Hobbywing
- **iFlight**: motors from iFlight
- **KDE**: motors from KDE Direct
- **Lumenier**: motors from Lumenier
- **Sunnysky**: motors from Sunnysky
- **TMotor**: motors from T-Motor
- **Turnigy**: motors from Turnigy
- **unknown**: unknown brand name

Note that this prefix will also be used to organize the csv data into folders.

## motor name
The motor name listed here should aim to be consistent with the product page. Any special characters should be replaced with a "-" and any spaces should be replaced with a "_" character. 
## motor name suffix
The motor name suffix should include anything that may vary with that model of motor. For example revision or KV. This may be empty if there is only one version of that motor model.
## date accessed
This should be the date that the motor data was accessed in YYYYMMDD format (for example today 12/31/2024 would be 20241231).