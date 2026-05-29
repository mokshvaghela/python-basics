# If the names of 2 friends are same; what will happen to the program in problem 6?

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

# Answer: If the names of 2 friends are the same, the program will overwrite the previous entry in the dictionary with the new entry.
# This is because dictionary keys must be unique. When a new entry with the same key is added, 
# It will replace the existing entry associated with that key. 
# Therefore, only the last entry for that name will be stored in the dictionary.