# How do you prevent a python print() function to print a new line at the end.

def print_without_newline():
    print("Hello, World!", end="")  # The 'end' parameter is set to an empty string to prevent a new line.
    print(" This will be printed on the same line.")

print_without_newline()