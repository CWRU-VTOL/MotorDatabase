# === Imports ===
import os
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd  # Optional: for table processing

# === Global Constants ===
BASE_URL = "https://www.kdedirect.com/collections/uas-multi-rotor-brushless-motors" # URL where the grid is 

# === Main Functions ===

# fetches motor price, name in string format, and url, for each item in the grid.
# creates gridData.csv in the local temp folder (overwrites if already present)
# this function will then create a column for each motor in csv file, following this format:
# row 1: URL row 2: name row 3: price (empty if unlisted)
def fetch_motors_from_grid(grid_page_url):
    create_empty_csv_file("MotorDatabase/scripts/data_acquisition/brand_specific/KDE/temp", "gridData.csv")

def fetch_motor_table(motor_link):
    pass

def fetch_performance_data(motor_link):
    pass


# === Utility Functions ===
#this function takes in the whole string of the motor and shortens it to the motor name that can be used for the file name.
def filter_motor_name(motor_name):
    pass
def is_ignored_motor(motor_name):
    pass

def create_folder(folder_path):
    pass

#creates new empty csv file if its empty, and replaces it with an empty file if it has contents
def create_empty_csv_file(target_dir, csv_name):
    # Define the target file path
    target_file = os.path.join(target_dir, csv_name)
    # Ensure the directory exists
    os.makedirs(target_dir, exist_ok=True)
    # Create (or overwrite) an empty CSV file
    with open(target_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Optionally, add headers here if needed
        # writer.writerow(["URL", "Name", "Price"])
    print(f"Empty gridData.csv file created at: {target_file}")



# === Main Script ===
def main():
    fetch_motors_from_grid("")
    

if __name__ == "__main__":
    main()
