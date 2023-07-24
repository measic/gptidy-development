##  for each row calculate Hill N21
for i in range(len(data)):
    N = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]
    #N2
    lam = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        lam += (data.iloc[i][x]/N) * (data.iloc[i][x]/N)
    N2 = 1/lam
        
    swi = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            swi += -(data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])) * math.log((data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])))
    N1 = math.exp(swi)
    
    data.loc[i,"N21"] = N2/N1