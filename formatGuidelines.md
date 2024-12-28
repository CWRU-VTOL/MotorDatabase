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
- Parameters fall into the following catagories
  - **required parameters** that must always be specified
  - **motor parameters** that are intrinsic to the motor and do not change per datapoint (such as kv or mass)
  - **performance parameters** that are specific to each datapoint, such as voltage, current, thrust, etc
  - **metadata parameters** that describe the source of each datapoint, such as if it is calculated (and if so how), or whose testing it's from, etc.
- Arbitrary column order is supported.
  - recommended column order for human readability is:
  -  required params | performance params | key motor params | other motor params | metadata params
- Blank cells will be interpreted as unknown/incomplete data.
- The parameters this format can support is highly extensible, although the currently supported ones are detailed below.

### Required Parameters

| Parameter     | Description                                                                        | Unit/Format   | Example                      |
|:--------------|:-----------------------------------------------------------------------------------|:--------------|:-----------------------------|
| motor_prefix  | Put brand name exactly from (brand name list to be made).                          | String        | SunnySky                     |
| motor_name    | Motor name, must not be blank                                                      | String        | SunnySky M8 Brushless Motors |
| motor_suffix  | Motor suffix for info like KV, revision model, etc. Fully standardize later/never. | KV-other      | 135KV                        |
| date_accessed | Date data was accessed for the motor. If missing, put current date.                | YYYYMMDD      | 20241228                     |

### Motor Parameters
| Parameter                         | Description                                                                                      | Unit/Format   | Example                                                                                        |
|:----------------------------------|:-------------------------------------------------------------------------------------------------|:--------------|:-----------------------------------------------------------------------------------------------|
| link                              | Link to where the motor can be bought and this data can be verified.                             | String        | https://www.kdedirect.com/collections/uas-multi-rotor-brushless-motors/products/kde10218xf-105 |
| kv                                | The KV rating of the motor.                                                                      | Int           | 135                                                                                            |
| total_weight                      | Total Weight of the motor.                                                                       | g             | 350                                                                                            |
| overall_diameter                  | Overall diameter of motor (of largest part).                                                     | mm            | 50                                                                                             |
| overall height                    | overall height of the motor                                                                      | mm            | 20                                                                                             |
| max_power                         | Maximum power output of the motor (assumed continuous).                                          | W             | 1000                                                                                           |
| min_voltage                       | Minimum rated operating voltage, otherwise assumed 0.                                            | V             | 12                                                                                             |
| max_voltage                       | Maximum allowed operating voltage.                                                               | V             | 25.2                                                                                           |
| max_thrust                        | Maximum thrust the motor can produce at its rated power.                                         | g             | 2500                                                                                           |
| max_current                       | Maximum current draw of motor (assumed continuous).                                              | A             | 40                                                                                             |
| min_prop_diameter                 | Minimum rated prop diameter                                                                      | inches        | 12                                                                                             |
| max_prop_diameter                 | Maximum rated prop diameter                                                                      | inches        | 24                                                                                             |
| notes                             | important additional notes about the motor                                                       | String        | Mounting holes M3.                                                                             |
| no_wire_weight                    | total weight of the motor without wires.                                                         | g             | 300                                                                                            |
| rotor_inertia                     | the inertia of the rotor                                                                         | kgcm^2        | 3.78                                                                                           |
| allowable_duration                | Allowable duration to be operated under those conditions (typically applicable to max throttle). | seconds       | 120                                                                                            |
| motor_resistance                  | Effective internal reistance of the motor.                                                       | milliOhms     | 181                                                                                            |
| motor_poles                       | Number of magnetic poles that the motor has.                                                     | Int           | 12                                                                                             |
| motor_coils                       | Number of magnetic coils that the motor has.                                                     | Int           | 9                                                                                              |
| Kt                                | Torque constant for motor                                                                        | Nm/A          | 0.01                                                                                           |
| Ke                                | Back EMF constant for motor                                                                      | V/(rad/s)     | 0.05                                                                                           |
| Km                                | Motor constant (related to torque effiency and heat generation).                                 | Nm/sqrt(W)    | 0.25                                                                                           |
| no_load_current                   | No load current of motor.                                                                        | A             | 1                                                                                              |
| no_load_current_voltage           | The voltage at which the motor's no load current is measured.                                    | V             | 10                                                                                             |
| shaft_diameter                    | Diameter of output drive shaft.                                                                  | mm            | 10                                                                                             |
| screw_mount                       | Does the motor support screw mount (alternative is shaft mount with nut typcially).              | boolean       | yes                                                                                            |
| cooling_airflow                   | Minimum airflow speed in m/s needed to cool to allow maximum output.                             | m/s           | 2.23                                                                                           |
| wire_awg                          | wire awg of the motor's wires                                                                    | AWG           | 12                                                                                             |
| min_timing_advance                | minimum motor timing advance                                                                     | degrees       | 22                                                                                             |
| max_motor_timing_advance          | maximum motor timing advance                                                                     | degrees       | 30                                                                                             |
| min_drive_frequency               | minimum drive frequency of motor                                                                 | kHz           | 16                                                                                             |
| max_drive_frequency               | maximum drive frequency of motor                                                                 | kHz           | 32                                                                                             |
| single_takeoff_weight_recommended | recommended maximum single takeoff weight                                                        | g             | 1750                                                                                           |

### Performance Parameters 
| Parameter           | Description                                                                                      | Unit/Format   | Example       |
|:--------------------|:-------------------------------------------------------------------------------------------------|:--------------|:--------------|
| voltage             | Voltage of the motor for a specific datapoint                                                    | V             | 22            |
| current             | current of the motor for a specific datapoint                                                    | A             | 12            |
| throttle            | Throttle percentage for a given datapoint.                                                       | %             | 75            |
| power               | electrical power consumed by the motor for a datapoint (V*I)                                     | W             | 350           |
| thrust              | thrust for a given datapoint                                                                     | g             | 1200          |
| thrust_at_sea_level | mostly for motors like KDE which specify different thrust values at sea level                    | g             | 1300          |
| efficiency          | thrust efficiency of the motor at a given datapoint, calculated                                  | g/W           | 8             |
| rpm                 | motor rpm for given datapoint                                                                    | rpm           | 6000          |
| torque              | torque to drive the propeller for a given datapoint                                              | Nm            | 1             |
| prop_diameter       | propeller diameter                                                                               | inches        | 22            |
| prop_pitch          | propeller pitch angle                                                                            | inches        | 6.3           |
| prop_blade_count    | propeller blade count                                                                            | Int           | 2             |
| prop_isfolding      | is the propeller folding?                                                                        | boolean       | no            |
| prop_iscarbon       | is the propeller carbon fiber (otherwise assumed polymer)                                        | boolean       | no            |
| prop_name           | exact propeller name                                                                             | String        | KDE-DPA-ML-M4 |
| prop_weight         | weight of the specified parameters                                                               | g             | 100           |
| temperature         | Max motor temperature reached under those conditions                                             | deg Celcius   | 60            |
| allowable_duration  | Allowable duration to be operated under those conditions (typically applicable to max throttle). | seconds       | 120           |
| ambient_temp        | ambient temperature for the test                                                                 | deg Celcius   | 22            |
| ambient_pressure    | ambient pressure where testing occured                                                           | atm           | 1             |

### Metadata Parameters
For now, the metadata parameters will consist of any parameter listed there with "_source" added to the end of it.

For example, power_source might contain the string "calculated VxI" to represent that the electrical power consumed was calculated in this manner.

This may be speficied later in more detail.
