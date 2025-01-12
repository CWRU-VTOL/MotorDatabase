"""
file_utils.py

This module provides utility functions for reading and writing various file types, with a focus on csv files. 
It is designed to be imported and used in other scripts, but it also contains a main function for testing purposes.

Functions:
- readcsv(input_path, output_format="list")
- writecsv(file_path, contents, overwrite_empty=True, overwrite_existing=True)

Example Usage:
    import file_utils
    data = file_utils.readcsv("/absolute/path/to/file.csv", output_format="list")
    file_utils.writecsv("/absolute/path/to/output.csv", data)

"""

import csv
import os

def readcsv(input_path, output_format="list"):
    """
    Reads a CSV file from the absolute path of input_path.

    Args:
        input_path (str): Absolute path to the input CSV file.
        output_format (str): Format of the returned data. Can be 'list' or 'dict'. Defaults to 'list'.

    Returns:
        list: A list of lists (for 'list') or a list of dictionaries (for 'dict').

    Raises:
        ValueError: If the output_format is not 'list' or 'dict'.
        FileNotFoundError: If the file at input_path does not exist.
    """
    if not os.path.isabs(input_path):
        raise ValueError("input_path must be an absolute path.")

    if output_format not in ["list", "dict"]:
        raise ValueError("output_format must be 'list' or 'dict'.")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file at {input_path} does not exist.")

    with open(input_path, mode="r", newline="", encoding="utf-8") as csvfile:
        if output_format == "list":
            reader = csv.reader(csvfile)
            return [row for row in reader]
        elif output_format == "dict":
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

def writecsv(file_path, contents, overwrite_empty=True, overwrite_existing=True):
    """
    Writes data to a CSV file at the absolute file_path.

    Args:
        file_path (str): Absolute path to the output CSV file.
        contents (list): Data to write. Must be a list of lists or a list of dictionaries.
        overwrite_empty (bool): Whether to overwrite empty cells in an existing file. Defaults to True.
        overwrite_existing (bool): Whether to overwrite non-empty cells in an existing file. Defaults to True.

    Raises:
        ValueError: If contents is not in an expected format (list of lists or list of dicts).
        ValueError: If file_path is not an absolute path.
    """
    if not os.path.isabs(file_path):
        raise ValueError("file_path must be an absolute path.")

    if not isinstance(contents, (list, tuple)) or not all(isinstance(row, (list, dict)) for row in contents):
        raise ValueError("contents must be a list of lists or a list of dictionaries.")

    file_exists = os.path.exists(file_path)

    if not file_exists:
        # Create and write new file
        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            if isinstance(contents[0], dict):
                writer = csv.DictWriter(csvfile, fieldnames=contents[0].keys())
                writer.writeheader()
                writer.writerows(contents)
            else:
                writer = csv.writer(csvfile)
                writer.writerows(contents)
        return

    # Read existing data
    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        existing_data = list(csv.reader(csvfile))

    # Prepare updated data
    if isinstance(contents[0], dict):
        headers = existing_data[0] if existing_data else contents[0].keys()
        new_data = [dict(zip(headers, row)) for row in existing_data[1:]] if existing_data else []

        for new_row in contents:
            for existing_row in new_data:
                for key in headers:
                    if key in new_row:
                        if overwrite_existing or (not existing_row[key] and overwrite_empty):
                            existing_row[key] = new_row[key]

        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(new_data)

    else:
        # List of lists handling
        max_rows = max(len(existing_data), len(contents))
        max_cols = max(len(row) for row in existing_data + contents)

        updated_data = [["" for _ in range(max_cols)] for _ in range(max_rows)]

        for i, row in enumerate(existing_data):
            for j, cell in enumerate(row):
                updated_data[i][j] = cell

        for i, row in enumerate(contents):
            for j, cell in enumerate(row):
                if overwrite_existing or (not updated_data[i][j] and overwrite_empty):
                    updated_data[i][j] = cell

        with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_data)

if __name__ == "__main__":
    # Example usage for testing purposes
    sample_data_list = [["Name", "Age"], ["Alice", "30"], ["Bob", "25"]]
    sample_data_dict = [{"Name": "Alice", "Age": "30"}, {"Name": "Bob", "Age": "25"}]

    # Testing readcsv and writecsv
    writecsv("/absolute/path/to/test.csv", sample_data_list)
    data = readcsv("/absolute/path/to/test.csv", output_format="list")
    print(data)
