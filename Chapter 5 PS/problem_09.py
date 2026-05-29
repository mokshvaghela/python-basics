# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Moksh", [1,2]}
s[4][0] = 3  # This will raise an error because sets are immutable and lists cannot be elements of a set

# Answer: No, we cannot change the values inside a list which is contained in a set because sets are immutable and do not allow mutable types like lists as elements.
