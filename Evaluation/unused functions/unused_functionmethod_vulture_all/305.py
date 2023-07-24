def max_corr(corr_list):
    max = 0
    for item in corr_list.iteritems():
        if item[1][1] > max:
            max = item[1][1]
            max_factor = item[1]
    return max_factor