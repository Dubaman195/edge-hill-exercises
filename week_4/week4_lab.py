'''Goal: Create a simple "Number Guessing Game"'''

# Define game function
def number_guessing_game():
    # Set secret number
    secret_number = 67

    # Start the loop
    while True:
        # Take user input
        num = int(input("Guess the secret number (between 1 and 100): "))

        # Check user input
        if num == secret_number:
            print("Congratulations! You guessed it!")
            break   # Exit the loop if correct

        elif num > secret_number:
            print("Too high! Try again.")

        else:
            print("Too low! Try again.")


# number_guessing_game()

'''Celcius to Fahrenheit Converter'''

# Define conversion function (c is celsius, f is fahrenheit)
def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32  # Conversion formula
    return f            # Return fahrenheit value to where function was called

# Set temperature in celsius
c_temp = 25
# Call function and store result
f_temp = celsius_to_fahrenheit(c_temp)

print(f"{c_temp}C is equal to {f_temp}F")

'''Local and Global Variables'''

my_variable = "I am global"

def test_scope():
    my_variable = "I am local"
    print(my_variable)

test_scope()
print(my_variable)

"""The print statements produce different outputs because one of them is being used inside the
function (a local variable) where the variable is overwrittenby a value inside and only inside
the function, while the outside variable (global variable) remains unchanged since whatever
happens inside a function does not affect the outside."""

'''Goal: Create a calculator where each operation is its own function'''

# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        # Handle division by zero
        return "Error! Cannot divide by zero." 
    
# Main loop
while True:
    # Take user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: ")) # Convert input to float for decimal support
    # Take operator input
    print("Select operator:\n+. Add\n-. Subtract\n*. Multiply\n/. Divide\n")
    operator = input("Enter choice: ")                  

    if operator == "+":
        print(f"The result is: {add(num1, num2)}")      # Call add function
    elif operator == "-":
        print(f"The result is: {subtract(num1, num2)}") # Call subtract function
    elif operator == "*":
        print(f"The result is: {multiply(num1, num2)}") # Call multiply function
    elif operator == "/":
        print(f"The result is: {divide(num1, num2)}")   # Call divide function
    else:
        print("Invalid input. Please try again.")       # Invalid operator handling

    if (input("Enter 'q' to quit or any other key to continue: ")) == 'q': # Exit condition
        break
