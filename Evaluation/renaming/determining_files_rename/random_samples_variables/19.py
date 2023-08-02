for i in range(len(data)):
    variable_def = 0.0
    for x in range(len(data.iloc[0]))[4:last]:
        if data.iloc[i][x] > 0:
            variable_def += -(data.iloc[i][x] / sum(data.iloc[i][4:last][data.iloc[i][4:last] > 0])) * math.log(data.iloc[i][x] / sum(data.iloc[i][4:last][data.iloc[i][4:last] > 0]))
    data.loc[i, 'SWI_e'] = variable_def