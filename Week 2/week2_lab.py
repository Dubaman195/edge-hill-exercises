# Exercise 1: Python Syntax & Comments

def exercise1():

    """
    This program converts a temperature from Celsius to Fahrenheit.
    """

    celsius = 25                        # Temperature in Celsius

    fahrenheit = (celsius * 9/5) + 32   # Convert to Fahrenheit

    """
    Changing the temperature to 0 degrees Celsius changes the result to 32 degrees Fahrenheit.
    Changing the temperature to 100 degrees Celsius changes the result to 212 degrees Fahrenheit.
    """

    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")    # Output the result

    main()


# Exercise 2: Data Types & Variables

def exercise2():

    string_example = "Hello, World!"    # This is a string
    integer_example = 42                # This is an integer
    float_example = 3.14                # This is a float
    boolean_example = True              # This is a boolean

    print(f"This is a {type(string_example)} example: {string_example}")    # Output the string example
    print(f"This is an {type(integer_example)} example: {integer_example}") # Output the integer example
    print(f"This is a {type(float_example)} example: {float_example}")      # Output the float example
    print(f"This is a {type(boolean_example)} example: {boolean_example}")  # Output the boolean example

    """
    Python allows you to change data types as it can be helpful for outputting different types of information into the console since when combined with other characters, it has to be a string.
    Additionally, if a user inputs data in the terminal, its also inputted in string format. This means that if you want to do any calculations with the inputted data, you have to change it to an integer or float.
    """

    main()


# Exercise 3: String Formatting

def exercise3():

    name = "Jayden"                 # My Name
    course = "Software Engineering" # Course name
    fav_language = "PHP"            # Favorite programming language
    fav_movie = "Iron Man 2"        # Favorite movie

    print(f"Hello, my name is {name}. I am currently enrolled in the {course} course. My favorite programming language is {fav_language} and my favorite movie is {fav_movie}.")

    main()


# Exercise 4: Decision Making (if / elif / else)

def exercise4():

    age = int(input("Please enter your age: "))  # Get user input for age

    if age < 0:         
        print("Invalid age. Please enter a valid age.")
        
    elif age < 13:
        print("You are a child.")           # Output if age is less than 13

    elif age < 20 and age >= 13:
        print("You are a teenager.")        # Output if age is between 13 and 19

    elif age < 65:      # nested if statement example
        if age >= 20:
            print("You hold unc status.")   # Output if age is between 20 and 64

    else:
        print("You are old.")               # Output if age is 65 or older

    """
    This input has no validation, so if you were to input a non-integer value, it would cause an error.
    """

    main()


# Main function to run the exercises based on user input

def main():

    answer = input("Please choose an exercise to run (1-4) or 'q' to quit:" \
                    "\n1. Exercise 1: Python Syntax & Comments" \
                    "\n2. Exercise 2: Data Types & Variables" \
                    "\n3. Exercise 3: String Formatting" \
                    "\n4. Exercise 4: Decision Making (if / elif / else)" \
                    "\nYour choice: ")

    match answer:
        case '1':
            exercise1()

        case '2':
            exercise2()

        case '3':
            exercise3()

        case '4':
            exercise4()
            
        case 'q':
            print("Exiting the program...")
            exit()

        case _:
            print("Invalid choice. Please select a valid exercise number (1-4) or 'q' to quit.")
            main()


main()  # Runs the program