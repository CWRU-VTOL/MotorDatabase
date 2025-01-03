"""
process_preliminary_csv.py

This script will validate the input data, which is a "preprocessed csv" file. 
Validatons to be implemented.
If it is valid then it will process it by putting it into the correct columns
and performing some calculations on the input data, then outputting it to an 
output csv.

Todo:
- validation function that does more than return true
- handle file path edge cases (cannot find files to read/write, or have permissions, etc)
- maybe add ability to specify details for validation and calculations/specifics of processing

Usage:
    As a standalone script:
        python process_preliminary_csv.py input_file reference_file output_file

    As a library:
        from process_preliminary_csv import validate_data, process_csv

Arguments:
    input_file  The path to the input CSV file.
    reference_file The path to the  reference file, expected to be template.csv probably. 
    output_file The path to save the processed CSV file.

Author:
    Simon
"""

import csv
import sys
import argparse

# helper functions
def read_csv(input_file):
    """Reads a CSV file and returns its contents as a list of dictionaries."""
    data = []
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data

def write_csv(output_file, data):
    """Writes processed data to a new CSV file."""
    if not data:
        print("No data to write.")
        return
    
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing file: {e}")

#main functions
def validateData(input_data, template_header):
    if (True):
        return True,""
    else:
        return False, "some error"
    
def process_data(input_data, template_header):
    """
    Does two main things
    1. copies corresponding columns in input_data into the correct template formatted output
    2. performs calculations where possible (power, efficiency, more to be added later)
    """
    processed_data = template_header
    for row in data:
        # Example: Add a new column 'Processed' with a value
        row['Processed'] = 'Yes'
        processed_data.append(row)
    return processed_data

def process_csv(input_path,reference_path,output_path):
    """
    all paths must be absolute
    input_path is the path to the input csv
    reference_path is the path to the reference csv (expected template.csv)
    output_path is the expected path to write the processed data to
    if the output file already exists it will be replaced, and it may be the same as the input files
    """    
    #note that all the data is treated as strings
    input_data = read_csv(input_path)
    template_header = read_csv(reference_path)
    isValid, errorMessage = validateData(input_data, template_header)
    if isValid:
        output_data = process_data(input_data, template_header)
        write_csv(output_data,output_path)
    else:
        print(errorMessage)

def main():
    parser = argparse.ArgumentParser(description="See documentation for details, processes preprocessed csv.")
    parser.add_argument("input_path", nargs="?", default=None, help="Input file abs path.")
    parser.add_argument("reference_path", nargs="?", default=None, help="Reference file abs path.")
    parser.add_argument("output_path", nargs="?", default=None, help="Reference file abs path.")
    args = parser.parse_args()
    process_csv(args.input_path,args.reference_path,args.output_path)



if __name__ == '__main__':
    main()
