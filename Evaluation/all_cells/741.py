##  for each row calculate 1-Lambda
for i in range(len(data)):
    N = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]

    lam = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        lam += (data.iloc[i][x]/N) * (data.iloc[i][x]/N)
    data.loc[i,'1-lam'] = 1 - lam