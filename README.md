# MotorDatabase
Welcome to **MotorDatabase** — a repository aimed at providing a **standardized CSV format** for UAV motor performance data. This database is designed to be both **human-readable** and **automation-friendly**, as it is aimed at UAV design and optimization.

## Overview
For many commercial and hobby UAV motors, manufacturers typically specify performance using static thrust data. However, this data is often highly **non-standardized**. Some manufacturers only provide **maximum thrust** and **KV ratings**. Others include more detailed parameters like **temperature**, **reaction torque**, and **efficiency**.

The lack of standardization can make comparing motors challenging. **MotorDatabase** addresses this issue by:
1. Providing a **consistent CSV format** for motor specifications.
2. Including scripts for **data processing** and **conversion**.
3. Hosting CSV files for a wide variety of motor brands.

## Features
- **Standardized Format**:
  - Ensures consistency across all motor data, following **formatGuidelines.md**.
  - Handles missing parameters gracefully.
- **Automation-Friendly**:
  - Easily integrates with data analysis pipelines.
- **Human-Readable**:
  - Clear organization for quick manual inspection.
- **Extensible**:
  - Allows inclusion of additional parameters as needed.

## Repository Structure
The repository is organized as follows:
```
MotorDatabase/
├── csv/                # Contains standardized motor CSV files
│   ├── [example_motor].csv
│   └── ...
├── scripts/            # Data processing and conversion scripts
│   ├── convert_to_csv.py
│   ├── validate_csv.py
│   └── ...
├── README.md           # Project documentation
├── formatGuidelines.md # Naming conventions and data format specifications
└── LICENSE             # Licensing information
```

## Usage
### For CSV Data
- CSV files are stored in the `csv/` directory.
- Each file is named according to the naming convention (todo: specify file naming convention).

### For Scripts
- Data processing and conversion scripts are located in the `scripts/` directory.
- Example: Run `convert_to_csv.py` to convert manufacturer formats into the standardized CSV format.

---

## Contributing
todo: add contribution guidelines

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments 
- (todo: as features implemented, be sure to update)

