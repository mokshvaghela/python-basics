# Set methods

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# 1. union() method - returns a set that contains all the items from both sets, without duplicates.
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
# 2. intersection() method - returns a set that contains only the items that are present in both sets.
print(s1.intersection(s2)) # {4, 5}
# 3. add() method - adds an element to the set. If the element already exists, it does nothing.
s1.add(6) # adds an element to the set
# 4. remove() method - removes the specified element from the set. If the element does not exist, it raises a KeyError.
s1.remove(6) # removes an element from the set
# 5. discard() method - removes the specified element from the set. If the element does not exist, it does nothing.
s1.discard(6) # removes an element from the set if it exists, otherwise does nothing
# 6. len() method - returns the number of items in the set.
print(len(s2)) # 5
# 7. pop() method - removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
print(s1.pop()) # removes and returns an arbitrary element from the set