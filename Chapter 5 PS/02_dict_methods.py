# Dictionary methods

marks = {
    "Moksh" : 67,
    "Jeet" : 89,
    "Priyam" : 78
}

# 1. keys() method - returns a view object that displays a list of all the keys in the dictionary.
print(marks.keys()) # dict_keys(['Moksh', 'Jeet', 'Priyam'])
# 2. values() method - returns a view object that displays a list of all the values in the dictionary.
print(marks.values()) # dict_values([67, 89, 78])
# 3. items() method - returns a view object that displays a list of dictionary's key-value tuple pairs.
print(marks.items()) # dict_items([('Moksh', 67), ('Jeet', 89), ('Priyam', 78)])
# 4. get() method - returns the value of the specified key. If the key does not exist, it returns None (or a specified default value).
print(marks.get("Moksh")) # 67
print(marks.get("Rohit")) # None
print(marks["Krishna"]) # KeyError: 'Krishna'
# 5. update() method - updates the dictionary with the specified key-value pairs. If the key already exists, it updates the value.
marks.update({"Veer" : 55})
# And many more methods like pop(), popitem(), clear(), copy(), etc.