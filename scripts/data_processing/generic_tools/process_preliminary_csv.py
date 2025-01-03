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
- maybe handle edge cases with template mistakes, mismatched row/cols, etc
- maybe add ability to specify details for validation and calculations/specifics of processing

Usage:
    As a standalone script:
        py process_preliminary_csv.py input_file reference_file output_file

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
    """
    Reads a CSV file and returns its contents as a list of lists of strings.
    
    Returns:
        list[list[str]]: Each inner list represents a row of the CSV, 
                         where the first row is the header.
    """
    data = []
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data

def write_csv(output_file, data):
    """
    Writes a list of lists of strings to a new CSV file. Overwrites old file if it existed.

    Args:
        output_file (str): Path to the output CSV file.
        data (list[list[str]]): Each inner list represents a row of the CSV, 
                                where the first row is the header.

    Returns:
        None
    """
    if not data:
        print("No data to write.")
        return

    try:
        if isinstance(output_file, list):
            raise TypeError(f"Expected a string or PathLike object for output_file, got {type(output_file)}")
        
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing file: {e}")


#main functions
def validateData(input_data, template_header):
    if (True):
        return True,""
    else:
        return False, "some error"

def copy_correct_columns(input_data, template_header):
    """
    Copies corresponding columns in input_data into the correct template formatted output.

    Args:
        input_data (list[list[str]]): Input data as a list of lists of strings, where the first row is the header.
        template_header (list[list[str]]): List of column headers for the template, only first row considered.

    Returns:
        list[list[str]]: Output data with columns arranged and matched to the template format.
    """
    # Initialize output data with the template header
    output_data = template_header

    # Pre-create empty rows in output_data for all rows in input_data (excluding header)
    for _ in range(len(input_data) - 1):
        output_data.append([""] * len(template_header[0]))  # Add empty rows with the correct number of columns


    for input_header_item_idx in range(len(input_data[0])): # iterate thru each header of input data
        for template_header_item_idx in range(len(template_header[0])): # iterate thru each header of the template
            if (input_data[0][input_header_item_idx]==template_header[0][template_header_item_idx]): # if the template header matches the input data header exactly
                input_col = [row[input_header_item_idx] for row in input_data[0:]]
                for data_item_idx in range(len(input_col)): #copy the column
                    if(input_col[data_item_idx].strip()): #if item is not empty
                        output_data[data_item_idx][template_header_item_idx] = input_col[data_item_idx] #copy it to output data
    return output_data

def format_data(input_data):
    """
    explain how data is formatted, prereqs for input data
    """
    #remove percentage symbols from throttle
    #correct that weird dash problem
    #maybe look and if its certain brands or formats like KDE, 
    #try to extract prop pitch and diameter etc from prop name
    return input_data

def calculate_formated_data(input_data):
    """
    performs calculations on correctly formatted columns (power, efficiency, more to be added later)
    """
    return input_data

def process_data(input_data, template_header):
    """
    Does two main things
    1. copies corresponding columns in input_data into the correct template formatted output
    2. performs calculations where possible (power, efficiency, more to be added later)
    """
    processed_data = copy_correct_columns(input_data, template_header)
    processed_data = format_data(processed_data)
    processed_data = calculate_formated_data(processed_data)

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
        write_csv(output_path,output_data)
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
