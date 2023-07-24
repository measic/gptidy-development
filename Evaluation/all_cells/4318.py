def winners_and_margins(dfClean):
    
    dfNew = pd.DataFrame(columns = ["STATE", "D", "WINNER", "MARGIN", "WINPER"])
    
    for i in range(len(dfClean)):
        row = dfClean.iloc[i]
        district = dfNew.loc[(dfNew["STATE"] == row["STATE"]) & (dfNew["D"] == row["D"])]
        
        if(district.empty):
            dfRow = row[["STATE", "D"]]
            dfRow["WINNER"] = row["CANDIDATE NAME"]
            dfRow["MARGIN"] = 100
            dfRow["WINPER"] = row["GENERAL PERCENT"]
            dfNew = dfNew.append(dfRow)
        else:
            (Margin, WinPer) = dfNew.loc[district.index[0], ['MARGIN', 'WINPER']]
            if(WinPer < row["GENERAL PERCENT"]):
                dfNew.loc[district.index[0], 'WINPER'] = row["GENERAL PERCENT"]
            elif(Margin > WinPer - row["GENERAL PERCENT"]):
                dfNew.loc[district.index[0], 'MARGIN'] = WinPer - row["GENERAL PERCENT"]
    
    dfNew = dfNew.sort_values(by='MARGIN')
    dfNew.drop(['WINPER'], axis = 1, inplace = True)
    
    return dfNew

winners_and_margins(clean_election_data())