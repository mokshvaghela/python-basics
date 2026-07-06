'''
Functions with Arguments:
Functions can also take arguments (or parameters) which allow you to pass data into the function for processing. 
This makes functions more flexible and reusable.
'''

def greet(name, ending): # Here, 'name' is a parameter that will accept the user's name.
    print(f"Good day, {name}!") # This will greet the user with their name.
    print(ending)

greet("Alice", "Thank you for coming!") # Function Call: This will execute the greet function and pass "Alice" and "Thank you for coming!" as arguments.

# Here can we also take input from the user for the arguments instead of hardcoding them.
name = input("Enter your name: ")
ending = input("Enter your ending message: ")
greet(name, ending) # Function Call: This will execute the greet function and pass the user-provided name and ending message as arguments.