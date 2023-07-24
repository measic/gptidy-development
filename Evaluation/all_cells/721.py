##  for each row calculate Margalef Species Richness Index
for i in range(len(data)):
    data.loc[i,'Margalef'] = (len(data.iloc[i][4:last][data.iloc[i][4:last]>0])-1)/math.log(sum(data.iloc[i][4:last][data.iloc[i][4:last]>0]))
