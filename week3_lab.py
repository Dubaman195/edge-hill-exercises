"""
This file contains the code for the Week 3 lab exercises,
focusing on for loops, while loops, and GitHub integration.
"""

# Step 2: Counting with range()
# This loop prints numbers from 1 to 20, and uses a range and a for loop.
def range_counter():
    print("Exercise 1: For Loop")
    
    """for i in range(1, 11):"""
    for i in range(1, 21):
        print(i)


# Step 3: Summing a List
def summing_a_list():
    costs = [15.00, 12.50, 3.75, 40.25, 6.99]
    total_cost = 0

    for i in costs:
        total_cost += i
    
    print(f"Total cost: ${total_cost:.2f}")


"""Exercise 3: Nested for lops - Pattern Generation"""

# Step 1: Create a simple square

def square_generator():
    size = 5
    for i in range(size):
        for x in range(size):
            print('*', end="")

        print()  # Move to the next line after each row

# Step 2: Create a right-angled triangle

def triangle_generator():
    size = 5
    for i in range(1, size + 1): # each iteration increases the range (and stars) by 1
        for x in range(i):
            print('*', end="")

        print()  # Move to the next line after each row


"""Exercise 4: The while Loop - Menu-Driven Calculator"""

def calculator():
    q = ""
    while q != "q":
        print("--- Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("q. Quit")
        q = input("Choose an option: ")

        if q == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The sum is: {num1 + num2}")

        elif q == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The difference is: {num1 - num2}")

        else:
            if q != "q":
                print("Invalid option, please try again.")
        
    print("Goodbye!")

calculator()