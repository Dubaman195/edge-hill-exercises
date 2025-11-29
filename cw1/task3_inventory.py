"""
You have been hired as a Junior Developer for a retail logistics company. They have a legacy
system that exports product data into a raw JSON file. Your manager needs a Python script
that can:
1. Load this data into your program.
2. Analyze the data to generate key business insights.
3. Update the inventory levels based on a simulated delivery.
4. Save the updated data back to a new file.
This task moves beyond simple syntax; it requires you to produce a viable program that
solves a data problem (LO3) using your development environment (LO4).
"""

import json


# Part A
def load_inventory(filename):
    """
    Load the inventory with error handling.

    Parameters:
        filename (str): A string containing a file name

    Returns:
        data (list): A list of dictionaries from JSON format
    """
    # Opens the JSON file
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data

    # Exception if file can't be found
    except FileNotFoundError as e:
        print(f"{filename} was not found: {e}")
        return []

    # Exception if file fails to load
    except Exception as e:
        print(f"Failed to load {filename}: {e}")
        return []


# Part B
def generate_report(data):
    """
    Generates report for:
    - Total item stock
    - Most expensive item
    - Out of stock items

    Parameters:
        data (list): A list of dictionaries in JSON format
    """
    # Calculates total stock
    total_stock = sum(i["stock"] for i in data)  # sums all "stock" in list
    print(f"The total amount of items in inventory is: {total_stock}")

    # Finds item with the highest price
    highest_price = 0
    highest = ""

    for i in data:
        # if current item's value is higher than logged highest
        if i["price"] > highest_price:
            highest_price = i["price"]  # replace the value
            highest = i["name"]         # make note of the name
    print(f"The most expensive item is: {highest}")

    # Creates list of out-of-stock items
    out_of_stock = []

    for i in data:
        if i["stock"] == 0:
            out_of_stock.append(i["name"])
    print(out_of_stock)


# Part C
def restock_item(data, product_id, amount):
    """
    Takes user inputs and updates stock values through the product ID.

    Parameters:
        data (list): A list of dictionaries in JSON format
        product_id (int): An integer
        amount (int): Another integer
    """
    found_id = False

    # Adds stock to id matching product_id
    for i in data:
        if i["id"] == product_id:
            i["stock"] += amount
            print(f"Restocked {i['name']}. New stock: {amount}")
            found_id = True

    # Handling if the product_id doesn't match any ids
    if not found_id:
        print("ID not found.")


# Part D
def save_inventory(filename, data):
    """
    Saves changes made to loaded file into another file.

    Parameters:
        filename (str): A string containing a file name
        data (list): A list of dictionaries in JSON format
    """
    # Creates or edits file with any made edits
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)  # enters list as JSON format into file


if __name__ == "__main__":
    data = load_inventory("inventory.json")
    print(data)

    generate_report(data)

    while True:
        print("---- Item Restocker ----")
        try:
            product_id = int(input("Please enter the product ID:\n"))
            amount = int(input("Please enter the amount to restock:\n"))
            break
        except:
            print("Please enter a number.")

    restock_item(data, product_id, amount)

    save_inventory("updated_inventory.json", data)
