# Format Guidelines

This document provides guidelines for naming conventions and CSV format specifications for the MotorDatabase project.

## Naming Convention for File Names
(program TBD) will automatically determine the correct file name based on the following parameters:
- motor name
- motor name suffix
- motor name prefix
- date accessed
the details for specifying each of these will be determined later

## CSV Contents and Organization

### Overall rules and structure:
- Each CSV file specifies the performance and parameters of one specific model of a motor, possibly with a number of different voltages and propeller combinations. 
- Commas are never allowed, spaces and standard characters are handled. 
- Every parameter is listed at the top as the column header. Parameter specification is detailed below

### Parameter specification overview
- The column order does not matter.
- Blank cells will be interpreted as unknown/incomplete data.
- Parameters always constant for a given motor only need to be specified once in row 2 (e.g. motor weight)
- A few key parameters are required to be specified, while the majority are optional.
- The parameters this format can support is extensible, although the currently supported ones are detailed below.

### Required parameters
- put stuff like motor naming, date accessed, and kv

### Optional parameters
- stuff like motor weight, thrust, etc

