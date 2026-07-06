# Default Arguments in Python:
'''
Default arguments are values that are assigned to parameters in the function definition. 
If no argument is passed for a default parameter, the default value is used.
'''
def greet(name, ending="Thank you for coming!"): # Here, 'ending' has a default value.
    print(f"Good day, {name}!") # This will greet the user with their name.
    print(ending)

greet("Alice") # Function Call: This will execute the greet function and pass "Alice" as an argument. The default value for 'ending' will be used.

greet("Bob", "Have a great day!") # Function Call: This will execute the greet function and pass "Bob" and "Have a great day!" as arguments.