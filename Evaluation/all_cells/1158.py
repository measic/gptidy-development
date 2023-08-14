def PreProcess(table,Dream9):
    #Select all variables that are not Categorical
    Tables=[table[[v for v in table.keys() if v not in Categorical]]]
    
    #Convert yes/no to 1/0
    Alias_Dict={'SEX':{'F':1},'PRIOR.MAL':{'YES':1},'PRIOR.CHEMO':{'YES':1},'PRIOR.XRT':{'YES':1},
                'Infection':{'Yes':1},'ITD':{'POS':1,'ND':numpy.nan},'D835':{'POS':1,'ND':numpy.nan},
                'Ras.Stat':{'POS':1,'NotDone':numpy.nan},'resp.simple':{'CR':1},'Relapse':{'Yes':1},
                'vital.status':{'A':1}}
    
    Tables+=[alias(table,Alias_Dict)]
    
    #Split data that has multiple values
    Tables+=[split(table['cyto.cat'],Dream9)]
    
    #Create new data for protein
    Tables+=[squared(table[Protein])]
    Tables+=[absolute(table[Protein])]
    Tables+=[bin_independent(table[Protein],Dream9,2)]
    Tables+=[bin_independent(table[Protein],Dream9,3)]
    Tables+=[bin_independent(table[Protein],Dream9,4)]
    Tables+=[bin_independent(table[Protein],Dream9,5)]
    
    #Make PCA axis
    Tables+=[make_pca(table[Protein],Dream9,200,name='PCA')]
    Tables+=[make_pca(table[Protein],Dream9,200,name='Whiten_PCA',whiten=True)]
    Tables+=[make_pca(squared(table[Protein]),squared(Dream9[Protein]),200,name='PCA_Sq')]
    
    #Bin dependent variables
    try:
        Tables+=[cutoff(table[['Overall_Survival','Remission_Duration']],130)]
        Tables+=[binned(table[['Overall_Survival','Remission_Duration']])]
    except KeyError:
        pass        
    
    #Join everything
    return pandas.concat(Tables,axis=1)