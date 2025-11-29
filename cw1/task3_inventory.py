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
    try:
        with open(filename,"r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Failed to load inventory: {e}")
        return None
        
data = load_inventory("inventory.json")
print(data)

# Part B

def generate_report(data):
    total = 0
    for i in data:
        total += i["stock"]
    print(f"The total amount of items in inventory is: {total}")

    highest_price = 0
    highest = ""
    for i in data:
        if i["price"] > highest_price:
            highest_price = i["price"]
            highest = i["name"]
    print(f"The most expensive item is: {highest}")

    out_of_stock = []
    for i in data:
        if i["stock"] == 0:
            out_of_stock.append(i["name"])
    print(out_of_stock)

def restock_item(data, product_id, amount):
    found_id = False
    for i in data:
        if i["id"] == product_id:
            i["stock"] = amount
            print(f"Restocked {i["name"]}. New stock: {amount}")
            found_id = True
    if found_id != True:
        print("ID not found!")
        
generate_report(data)

