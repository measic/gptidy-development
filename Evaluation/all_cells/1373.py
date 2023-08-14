#This can be used to filter dir() to get the variables of the most interest to the typical user of JN. Don't worry about the details for now.
varlist = [x for x in dir() if '_' not in x]
print(varlist)