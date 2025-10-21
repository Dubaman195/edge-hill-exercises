# This script calculates the total expense from a list of individual expenses.

expenses = [12.50, 15.75, 9.99, 20.00, 5.25] # List of individual expenses
total_debt = 0 # Initialize total debt to zero

for debt in expenses: # Iterate through each expense
    total_debt += debt # Add each expense to total debt

print(f"The total expense is: ${total_debt:.2f}") # Print the total expense formatted to two decimal places

# Expected output: The total expense is: $63.49