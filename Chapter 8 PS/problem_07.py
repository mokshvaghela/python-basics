# Write a python function to remove a given word from a list and strip it at the same time.

def rem(list, word):
    # Use list comprehension to create a new list without the specified word
    # and strip any leading/trailing whitespace from the remaining words.
    n = []
    for i in list:
        if not i == word:
            n.append(i.strip(word))
    return n

list = [ 'apple', 'banana', 'cherry', 'date', 'apple' ]
print(rem(list, "app"))