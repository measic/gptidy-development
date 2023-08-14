#alternative, compact way to extract a range of columns using the list built from range() of consecutive numbers
# building a list explicitly as follows is not necessary but can help with debugging because you can see the list.
# print([x for x in range(0,3)]) 
E=D[:,range(0,3)]
print(E)