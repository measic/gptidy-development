##  for each row calculate Hill N-infinity
for i in range(len(data)):
    
    N = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            N += data.iloc[i][x]
    
    
    array = data.iloc[i][4:last]
    data.loc[i,'N_Inf'] = 1/(max(array)/N)