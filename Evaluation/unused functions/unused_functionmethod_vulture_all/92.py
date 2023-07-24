def cutoff(Table,cutoff):
    #This function makes values above a threeshold equal to the threeshold
    Tab=[]
    for key0 in Table.keys():
        Series=Table[key0]
        new_Series=Table[key0].copy()
        for key,data in zip(Series.keys(),Series):
            if data>cutoff:
                new_Series[key]=cutoff
            else:
                new_Series[key]=data
        new_Series.name='%s_cut'%Series.name
        Tab+=[new_Series]
    return pandas.concat(Tab,axis=1)

def binned(Table,bins=[0,52,104]):
    #This function will bin the results from Remission and Overall Survival as expected    
    Tab=[]
    for key0 in Table.keys():
        Series=Table[key0]
        bins = numpy.array(bins)
        digitized = list(numpy.digitize(Series, bins))
        for i,v in enumerate(Series):
            if numpy.isnan(v):
                digitized[i]=numpy.nan
        Tab+=[pandas.Series(digitized,index=Series.index,name='%s_binned'%Series.name)*52-26]
    return pandas.concat(Tab,axis=1)
#Example
#pandas.concat([Trial_data[Dependent[-2:]],cutoff(Trial_data[Dependent[-2:]],130),binned(Trial_data[Dependent[-2:]])],axis=1).T