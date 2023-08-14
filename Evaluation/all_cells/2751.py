def importInflunet(path):
    '''
    Reads the Influnet data and creates a unique multiindex dataframe of the format
    
    (year,week) - incidence
    
    :param path: location of the influnet folder
    :return: compacted version of 
    '''
    
    df = pd.concat([pd.read_csv(path+t, names=["time", "incidence"], sep=" ", header=1, usecols=[0,4], decimal=",") for t in listdir(path)], ignore_index=True)
    df[["year","week"]] = df["time"].str.split("-", expand=True).astype(int)
    df.drop(["time"], axis=1, inplace=True)
    df = df.set_index(["year","week"])
    df.sortlevel(inplace=True)
    df = df.astype(float)
    df = df.loc[2008:]
    return df

def padInflunet(aux, year):
    '''
    The influnet dataset lacks information about the weeks that do not belog to the flu season (usally, but not necessarly, from week 17 to 40).
    This functions fills the dataset with empty position in order to match the wikipedia format.
    
    :param aux: Influnet dataframe from a specific year
    :param year: year of the previous Influnet dataframe
    :return: padded version of the original dataframe
    '''
    year_weeks = aux.index.values[-1]
    week_range = range(1,year_weeks+1)
    aux = aux.reindex(week_range, fill_value=0)
    aux["year"] = year
    aux["week"] = week_range
    
    aux.set_index(['year', 'week'], append=False, inplace=True)
    return aux


def getInflunet(path = "/home/aalto/Desktop/DE/hw2/influnet/data/"):
    '''
    import and reformat the original Influnet dataset
    
    :param path: 
    :return: clean and padded version of the Influnet dataset
    '''
    
    df = importInflunet();
    previous = None
    for x,y in df.index.values:
        if previous == None:
            df2 = reindexDF(df.loc[x], x)
        elif x != previous:
            df2 = df2.append(reindexDF(df.loc[x], x))
        previous = x
    return df