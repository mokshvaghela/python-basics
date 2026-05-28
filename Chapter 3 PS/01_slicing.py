name = "Moksh"

shortname = name[0:3]
print(shortname)

name[:3]
print(name[:3])# is same as print(name[0:3])
print(name[1:])# is same as print(name[1:5])

# We can also use negative indexing in slicing
print(name[-5:-2]) # is same as print(name[0:3])
# But negative indexing is not used in slicing because it is not easy to understand. 
# It is better to use positive indexing in slicing.