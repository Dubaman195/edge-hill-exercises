"""
This file contains the code for the Week 3 lab exercises,
focusing on for loops, while loops, and GitHub integration.
"""

# Step 2: Counting with range()
# This loop prints numbers from 1 to 20, and uses a range and a for loop.
def exercise_1():
    print("Exercise 1: For Loop")
    
    """for i in range(1, 11):"""
    for i in range(1, 21):
        print(i)


# Step 3: Summing a List
def exercise_2():
    costs = [15.00, 12.50, 3.75, 40.25, 6.99]
    total_cost = 0

    for i in costs:
        total_cost += i
    
    print(f"Total cost: ${total_cost:.2f}")