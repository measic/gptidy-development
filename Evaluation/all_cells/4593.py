# Take a `list()` of a to make a new copy in memory and assign to b
a = [1,2,3]
b = list(a)
print(hex(id(a)))
print(hex(id(b)))