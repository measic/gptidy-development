def merge(dict1, dict2):
    result = dict1
    for key, value in dict2.iteritems():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

def antisymmetries(mu):
    mu = Partition(mu)
    return antisymmetries_of_tableau(mu.initial_tableau())