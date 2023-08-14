def factor_with_high_corr(corr_list):
    return_list = []
    for i in range(len(corr_list)):
        return_list.append(corr_list[i+1][0])
    return return_list