#  If languages of two friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter your name:")
lang = input("Enter your favourite language:")
d.update({name : lang})

name = input("Enter your name:")
lang = input("Enter your favourite language:")
d.update({name : lang})

name = input("Enter your name:")
lang = input("Enter your favourite language:")
d.update({name : lang})

name = input("Enter your name:")
lang = input("Enter your favourite language:")
d.update({name : lang})


print(d)

# Answer: If the languages of two friends are the same, the program will still work correctly.
# The dictionary will store the names as keys and their corresponding favorite languages as values.
# If two friends have the same favorite language, it will not affect the dictionary since the keys (names) are unique. 
# Each friend's name will still be associated with their favorite language, even if multiple friends share the same language.