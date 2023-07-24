mylist = []
with open(pathname, 'r') as infile:
    for line in infile:
        rowlist = line.split()
        #this applies a filter to the list to eliminate non-alphanumeric items.
        rowclean = [x for x in rowlist if x.isalnum()]
        mylist.append(rowclean)
print(mylist)