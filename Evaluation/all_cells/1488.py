mylist = []
with open(pathname, 'r') as infile:
    for line in infile:
        mylist.append(line.split())
print(mylist)