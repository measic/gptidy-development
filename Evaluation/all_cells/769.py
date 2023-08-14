##  for each row calculate Hill N10 prime 
for i in range(len(data)):
    swi = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            swi += -(data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])) * math.log((data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])))
    try:
        data.loc[i,"N10'"] = (math.exp(swi)-1)/(len(data.iloc[i][4:last][data.iloc[i][4:last]>0])-1)
    except:
        data.loc[i,"N10'"] = 0