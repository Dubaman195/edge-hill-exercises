# WET Code Block - Hard to read!

"""
def start_scene():
    print("You are in a dark forest. You see two paths.")
    choice1 = input("Do you go 'left' or 'right'? ")
    if choice1 == 'left':
        left_path_scene()
    elif choice1 == 'right':
        right_path_scene()
    else:
        print("Invalid choice. You are lost.")


def left_path_scene():
    print("You walk down the left path and find a river.")
    choice2 = input("Do you 'swim' across or 'follow' the river bank? ")
    if choice2 == 'swim':
        print("You are tired from swimming and rest. You win!")
    elif choice2 == 'follow':
        print("You follow the river bank and find a hidden cave. You win!")
    else:
        print("Invalid choice. You are lost.")


def right_path_scene():
    print("You walk down the right path and encounter a sleeping bear.")
    choice2 = input("Do you 'tiptoe' past or 'run' away? ")
    if choice2 == 'tiptoe':
        print("You successfully sneak past the bear. You win!")
    elif choice2 == 'run':
        print("You trip while running and the bear wakes up. You lose.")
    else:
        print("Invalid choice. You are lost.")

start_scene()
"""

# BROKEN Code Block

player_score = 0 # This is a GLOBAL variable

def add_points(player_score):
    # Bug: This creates a new LOCAL variable
    player_score += 10
    print(f"[Inside Function] Score is now: {player_score}")
    return player_score

# --- Main Program ---
print(f"[Outside] Player score is: {player_score}")
player_score = add_points(player_score)
print(f"[Outside] Player score is: {player_score}") # Why is it still 0?

"""
Example: Creating a Flowchart and Pseudocode for a Simple Task

Before you start, let's look at a sample problem so you understand what's
expected.

Suppose we want to write a function that checks if a number is positive,
negative, or zero.

We'll first write the pseudocode, then draw the flowchart for it.

Pseudocode:
------------
START
    FUNCTION check_number(num):
        IF num > 0:
            PRINT "The number is positive."
        ELSE IF num < 0:
            PRINT "The number is negative."
        ELSE:
            PRINT "The number is zero."
    END FUNCTION
END

Now, we could draw the flowchart with these shapes:
    - Oval: Start / End
    - Parallelogram: Input or Output
    - Diamond: Decision (Is num > 0? Is num < 0?)
    - Rectangle: Process (e.g., setting variables or performing calculations)

Once you understand this example, try writing your own pseudocode and
flowchart for your chosen task

(e.g., add_new_item, view_all_items, or divide function with error
checking)
"""

"""
START
    FUNCTION stupid_idiot_calculator():
        PRINT "Welcome to the Stupid Idiot Calculator! What is your name?"
        INPUT name
        PRINT "Hello, " + name + "! You are about to use the Stupid Idiot Calculator."
        PRINT "What is your response?"
        INPUT response
        IF response == "huh":
            PRINT "You are stupid."
            PRINT "Goodbye, Idiot."
        ELSE:
            PRINT "You are not stupid."
            PRINT "Goodbye, " + name + "!"
    END FUNCTION
"""

"""
START
    FUNCTION age_egligibility_checker():
        PRINT "What is your age?"
        INPUT age
        IF age >= 18:
            PRINT "You are eligible to vote."
        ELSE:
            PRINT "You are not eligible to vote."
    END FUNCTION
"""