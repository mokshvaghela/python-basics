# Tuple methods

a = (23, 43, 45.4, 43, "Moksh")
print(a.count(43)) # 2 (counts the number of occurrences of 43 in the tuple)
print(a.index(45.4)) # 2 (returns the index of the first occurrence of 45.4 in the tuple)

repeated_tuple = a * 3
print(repeated_tuple)

# and there are many more methods that we can use with tuples.
# Tuples do not have methods like append, insert, remove, pop, reverse, sort etc. because they are immutable.