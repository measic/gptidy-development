for i in range(len(data)):
    variable_def = 0.0
    for x in range(len(data.iloc[i]))[4:last]:
        if data.iloc[i][x] > 0:
            variable_def += data.iloc[i][x]
    array = data.iloc[i][4:last]
    num = 0.0
    for y in array:
        num += y * (y - 1)
    lam = num / (variable_def * (variable_def - 1))
    data.loc[i, "lam'"] = lam