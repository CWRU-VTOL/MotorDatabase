# === Imports ===
import os
import csv
import requests
from bs4 import BeautifulSoup
#import pandas as pd  # Optional: for table processing

# === Global Constants ===
dateString = "20241231"
prefixString = "KDE"
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

def fetch_motor_table(grid_data_relative_path):

    # Open the CSV file
    with open(grid_data_relative_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        csv_data = list(reader)  # Convert the reader object to a list for easy indexing

        # Ensure the CSV has at least three rows
        if len(csv_data) < 3:
            print("CSV does not have enough rows.")
            return

        # Loop through the columns and check the value in the third row
        for col_idx in range(len(csv_data[0])):  # Loop through columns
            url = csv_data[0][col_idx]  # First row value (URL)
            name = csv_data[1][col_idx]  # Second row value (Name)
            price = csv_data[2][col_idx]  # Third row value (Price)

            if price.strip():  # Check if the price is not empty
                print(f"URL: {url}, Name: {name}, Price: {price}")
                csv_name = f"{get_file_name(prefixString,name,"table",dateString)}.csv"
                create_empty_csv_file("motor_specs", csv_name)
                fullUrl = f"https://www.kdedirect.com{url}"
                pathed_file_name = f"motor_specs\{csv_name}"
                extract_table(fullUrl,pathed_file_name)

def extract_table(url, csv_file_path):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Locate the specifications section and table
        specs_section = soup.find("section", id="specifications")
        if not specs_section:
            print(f"No specifications section found at {url}.")
            return

        table = specs_section.find("table")
        if not table:
            print(f"No table found in the specifications section at {url}.")
            return

        # Extract table rows and cells
        rows = table.find_all("tr")
        table_data = []
        for row in rows:
            cells = row.find_all(["td", "th"])  # Include table headers (th) and data (td)
            table_data.append([cell.get_text(strip=True) for cell in cells])

        # Write the table to the CSV file
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table_data)

        print(f"Table data successfully written to {csv_file_path}.")

    except requests.RequestException as e:
        print(f"Error fetching the URL {url}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_performance_data(motor_link):
    pass


# === Utility Functions ===

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

# this function will convert the "name" string to the full file name as specified in the format
#suffix will be "table" or "performance"
def get_file_name (prefix, unfiltered_name, suffix, date):
    filtered_name = unfiltered_name.split(" ")[0]  # Take everything before the first space
    filtered_name = filtered_name.replace(" ", "")  # Remove any remaining spaces
    filtered_name = filtered_name.replace("-", "_")  # Replace all '-' with '_'
    return f"{prefix}-{filtered_name}-{suffix}-{date}"

# === Main Script ===
def main():
    
    # create_empty_csv_file("temp", "gridData.csv")
    
    # fetch_motors_from_grid("https://www.kdedirect.com/collections/uas-multi-rotor-brushless-motors","temp\gridData.csv")
    
    # fetch_motor_table("temp\gridData.csv")
    pass
    

if __name__ == "__main__":
    main()
