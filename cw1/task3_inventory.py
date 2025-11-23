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

def load_inventory(filename):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
    except:
        print("poop")