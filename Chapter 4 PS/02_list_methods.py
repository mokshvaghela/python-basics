# List methods
# List methods are built-in functions that can be used to perform various operations on lists.

dataa = ["Moksh", 56, 2.6]
print(dataa) # ["Moksh", 56, 2.6]
dataa.append("Python") # Adds "Python" to the end of the list
dataa.insert(1, "is") # Inserts "is" at index 1
dataa.remove(56) # Removes the first occurrence of 56 from the list
dataa.pop() # Removes and returns the last item from the list
dataa.reverse() # Reverses the order of the list
print(dataa)

l1 = [34, 56 , 12 , 32 , 1, 5 , 7]
l1.sort() # Sorts the list in ascending order (only works if all elements are of the same type)
print(l1) # [1, 5, 7, 12, 32, 34, 56]