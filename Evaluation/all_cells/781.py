##  for each row calculate Pielou's Evenness Index 
for i in range(len(data)):

    count = 0.0
    hmax = 0.0
    
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            count += 1

    swi = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            swi += -(data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])) * math.log((data.iloc[i][x]/sum(data.iloc[i][4:last][data.iloc[i][4:last]>0])))

          
    data.loc[i,'Pielou'] = swi/math.log(count)





