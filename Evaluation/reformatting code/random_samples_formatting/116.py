def clean_election_data():
    '''
    Function to clean election data 
    '''
    import math
        
    # read in dirty data 
    df = pd.read_csv("2014_election_results.csv")
    dfClean = df.dropna(subset=["STATE", "D", "GENERAL PERCENT"]).copy()

    for i in range(len(dfClean)):
        row = dfClean.iloc[i]  
        row["GENERAL PERCENT"] = np.float(row["GENERAL PERCENT"].strip("%").replace(",", "."))
        if(pd.isnull(row["CANDIDATE NAME"]) or (row["CANDIDATE NAME"] == 'Scattered')):
            if(pd.isnull(row["CANDIDATE NAME (Last)"]) or (row["CANDIDATE NAME (Last)"] == 'Scattered')):
                row["CANDIDATE NAME"] = "UNKNOWN" 
            else:
                row["CANDIDATE NAME"] = row["CANDIDATE NAME (Last)"]
    
    dfClean = dfClean[["STATE", "D", "CANDIDATE NAME", "GENERAL PERCENT"]]
    return dfClean