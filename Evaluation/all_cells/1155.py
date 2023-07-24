def alias(Table,aliases):
    Aliased=[]
    for key in Alias_Dict:
        if key in Table.keys():
            Series=Table[key]
            new_Series=pandas.Series()
            new_Series.name=Series.name
            for key2,data in zip(Series.keys(),Series):
                new_Series[key2]=0.0
                for val in aliases[key]:
                    try:
                        if numpy.isnan(data):
                            new_Series[key2]=numpy.nan
                    except:
                        pass             
                    if data==val:
                        new_Series[key2]=aliases[key][val]
                        break
            Aliased+=[new_Series]
    return pandas.concat(Aliased,axis=1)
    
    #Changes the values on a Series with aliases as a dict that transform the old values in the new values
    

def split(Series,All_Data):
    #For Series with multiple values, creates a table with a column for each unique value
    #The value is True for the correct column and False for all the other columns
    D=[]
    for value in All_Data[Series.name].unique():
        q=(Series==value)*1.0
        q.name='%s=%s'%(q.name,value)
        D+=[q]
    return pandas.concat(D,axis=1)

#Example
#Alias_Dict={'SEX':{'F':1},'PRIOR.MAL':{'YES':1},'PRIOR.CHEMO':{'YES':1},'PRIOR.XRT':{'YES':1},
#                'Infection':{'Yes':1},'ITD':{'POS':1,'ND':numpy.nan},'D835':{'POS':1,'ND':numpy.nan},
#                'Ras.Stat':{'POS':1,'NotDone':numpy.nan},'resp.simple':{'CR':1},'Relapse':{'Yes':1},
#                'vital.status':{'A':1}}
#pandas.concat([Trial_data[Categorical[:4]+['cyto.cat']],alias(Trial_data,Alias_Dict),split(Trial_data['cyto.cat'],Dream9)],axis=1).T