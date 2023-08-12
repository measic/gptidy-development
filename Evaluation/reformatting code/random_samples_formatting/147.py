influnet = getInflunet()
influnet



x = wiki2.index[wiki2.index.year == 2010]
y = wiki2[wiki2.index.year == 2010]
    y2 = df2.loc[2010:][:len(x)]

comparePlots([influnet, wiki_influenza], [2010]) #needs to be in the right format