# === Imports ===
import os
import csv
import requests
from bs4 import BeautifulSoup
#import pandas as pd  # Optional: for table processing

# === Global Constants ===

# === Main Functions ===

# fetches motor price, name in string format, and url, for each item in the grid.
# creates gridData.csv in the local temp folder (overwrites if already present)
# this function will then create a column for each motor in csv file, following this format:
# row 1: URL (part after https://www.kdedirect.com)
# row 2: name row 3: price (empty if unlisted)
def fetch_motors_from_grid(grid_page_url, target_csv):
    try:
        # Fetch the grid page content
        response = requests.get(grid_page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the parent container (grid-uniform)
        grid_container = soup.find("div", class_="grid-uniform")
        if not grid_container:
            print("No grid container found.")
            return

        # Find all individual grid items
        grid_items = grid_container.find_all("div", class_="grid-item")
        if not grid_items:
            print("No grid items found.")
            return

        # Add columns for each grid item
        csv_data = []
        while len(csv_data) < 3:
            csv_data.append([])

        for item in grid_items:
            # Extract URL, name, and price (use correct tags and classes)
            url = item.find("a", class_="product-grid-item")["href"] if item.find("a", class_="product-grid-item") else ""
            name = item.find("p").text.strip() if item.find("p") else ""  # Extract name from <p> tag
            price_tag = item.find("span", class_="h1 medium--left")  # Replace with actual class for price
            price = price_tag.text.strip() if price_tag else ""

            # Append data as a new column
            if csv_data:
                for i, row in enumerate(csv_data):
                    if i == 0:
                        row.append(url)
                    elif i == 1:
                        row.append(name)
                    elif i == 2:
                        row.append(price)
            else:
                csv_data = [[url], [name], [price]]

        # Write updated data back to the CSV
        target_csv = os.path.abspath(target_csv)
        with open(target_csv, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(csv_data)

        print(f"Grid data added to {target_csv}")

    except requests.RequestException as e:
        print(f"Error fetching the grid page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    


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
    # Convert the target directory to an absolute path
    target_dir = os.path.abspath(target_dir)
    
    # Define the target file path
    target_file = os.path.join(target_dir, csv_name)
    
    # Ensure the directory exists
    os.makedirs(target_dir, exist_ok=True)
    
    # Create (or overwrite) an empty CSV file
    with open(target_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Optionally, add headers here if needed
        # writer.writerow(["URL", "Name", "Price"])
    
    print(f"Empty {csv_name} file created at: {target_file}")



# === Main Script ===
def main():
    create_empty_csv_file("temp", "gridData.csv")
    fetch_motors_from_grid("https://www.kdedirect.com/collections/uas-multi-rotor-brushless-motors","temp\gridData.csv")
    

if __name__ == "__main__":
    main()
