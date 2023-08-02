"""Function to compute half-life times of given nuclides"""

def function_def(fp_list, nuclides):
    ordered_fp_list = sorted(fp_list, key=lambda entry: entry.Z, reverse=False)
    half_life_1_10 = list()
    half_life_10_100 = list()
    half_life_100_1000 = list()
    half_life_1000_1M = list()
    half_life_1M_10M = list()
    half_life_10M_100M = list()
    half_life_100M_infty = list()
    for fp in ordered_fp_list:
        name = fp.name
        if name in nuclides.keys():
            nc = nuclides[name]
            element_name = nc.element_name
            h_f_y = nc.half_life / 3600 / 24 / 365
        else:
            element_name = fp.element_name
            h_f_y = 100000000.0 + 1 / 365
        save = (name, element_name)
        if h_f_y >= 1 and h_f_y < 10:
            half_life_1_10.append(save)
        elif h_f_y >= 10 and h_f_y < 100:
            half_life_10_100.append(save)
        elif h_f_y >= 100 and h_f_y < 1000:
            half_life_100_1000.append(save)
        elif h_f_y >= 1000 and h_f_y < 1000000.0:
            half_life_1000_1M.append(save)
        elif h_f_y >= 1000000.0 and h_f_y < 10000000.0:
            half_life_1M_10M.append(save)
        elif h_f_y >= 10000000.0 and h_f_y < 100000000.0:
            half_life_10M_100M.append(save)
        else:
            half_life_100M_infty.append(save)
    print('|    Half-Life     |  FP Nuclides   |')
    print('|:-----------------|:------------|')
    nuclides = str()
    for ele in half_life_1_10:
        nuclides += ele[0] + ', '
    print('|1 to 10 y         |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_10_100:
        nuclides += ele[0] + ', '
    print('|10 to 100 y       |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_100_1000:
        nuclides += ele[0] + ', '
    print('|100 to 1 ky       |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_1000_1M:
        nuclides += ele[0] + ', '
    print('|1 ky to 1 My      |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_1M_10M:
        nuclides += ele[0] + ', '
    print('|1 My to 10 My     |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_10M_100M:
        nuclides += ele[0] + ', '
    print('|10 My to 100 My    |', nuclides[:-2], '|')
    nuclides = str()
    for ele in half_life_100M_infty:
        nuclides += ele[0] + ', '
    return