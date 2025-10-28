# Example 1

def for_loop_example():
    
    total = 0
    for i in range(5):
        total = total + i
        print(total)


"""for_loop_example()"""


# Example 2

def for_loop_example_2():
    
    ids = [2659399, 2659400, 2659401, 2659402, 2659403, 2659404, 2659405, 2659406, 2659407, 2659408, 2659409]
    emails = []

    for i in ids:
        emails.append(f"{i}@edgehill.ac.uk")
    
    print(emails)


"""for_loop_example_2()"""


# Example 5

def function_param_example(width, height):
    
    area = width * height
    print(f"The area is: {area}")


"""function_param_example(5, 10)"""

