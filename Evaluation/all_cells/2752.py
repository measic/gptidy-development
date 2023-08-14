def getWiki(wikiPages, path = "/home/aalto/PycharmProjects/digitalepidemiology/data/"):
    '''
    
    :param wikiPages: list of the wikipages that we want to analyze
    :param path: location of the downloaded wikipedia pages
    :return: 
    '''
    df = pd.DataFrame()
    for wikiPage in wikiPages:
        wiki2 = pd.read_csv(path+wikiPage+".csv", usecols=[0,1], parse_dates=[0], index_col=[0], header=None)
        wiki2 = wiki2.resample("W-Sun").sum()
        df[wikipage] = wiki2
    return df