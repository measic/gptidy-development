# For each row, calculate Lambda Prime
for i in range(len(data)):
    N = 0.0
    for x in range(len(data.iloc[i]))[4:last]:
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]

    array = data.iloc[i][4:last]
    num = 0.0
    for y in array:
        num += (y * (y - 1))
    lam = num / (N * (N - 1))
    data.loc[i, "lam'"] = lam