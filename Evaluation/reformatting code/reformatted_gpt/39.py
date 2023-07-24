import pandas

def squared(Table):
    # This function squares all the values on a table
    D = []
    for i, var in enumerate(Table.keys()):
        D += [Table[var] ** 2]
        D[i].name = '%s_Squared' % var
    return pandas.concat(D, axis=1)

def absolute(Table):
    # This function squares all the values on a table
    D = []
    for i, var in enumerate(Table.keys()):
        D += [(Table[var] ** 2) ** 0.5]
        D[i].name = '%s_Absolute' % var
    return pandas.concat(D, axis=1)

# Example
# pandas.concat([Trial_data[Protein[:4]], squared(Trial_data[Protein[:4]]), absolute(Trial_data[Protein[:4]])], axis=1).T