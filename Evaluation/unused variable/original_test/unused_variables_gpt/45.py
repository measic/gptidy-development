##  for each row calculate Hill N2
for i in range(len(data)):
    N = 0.0
    for x in range(4, last):
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]

    lam = 0.0
    for x in range(4, last):
        lam += (data.iloc[i][x]/N) * (data.iloc[i][x]/N)
    data.loc[i,'N2'] = 1/lam