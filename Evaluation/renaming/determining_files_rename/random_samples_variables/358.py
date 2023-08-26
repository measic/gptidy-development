for i in range(len(data)):
    N = 0.0
    for x in range(len(data.iloc[i]))[4:last]:
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]
    array = data.iloc[i][4:last]
    variable_def = 0.0
    for y in array:
        variable_def += y * (y - 1)
    lam = variable_def / (N * (N - 1))
    data.loc[i, "lam'"] = lam