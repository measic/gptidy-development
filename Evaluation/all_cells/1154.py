import numpy,pandas
if __name__=='__main__':
    from sklearn.decomposition import PCA
    import numpy as np

    #For the preprocessing we need the data from Dream9.xlsx
    Dream9_training=pandas.read_excel('Dream9.xlsx',"trainingData") 
    Dream9_scoring=pandas.read_excel('Dream9.xlsx',"scoringData")
    Dream9=pandas.concat([Dream9_training,Dream9_scoring])

    #Division of types of Variables
    All=list(Dream9_training.keys())
    Sc=list(Dream9_scoring.keys())

    #Dependent variables are present in the training set but not in the scoring set
    Dependent=[]
    for v in All:
        if v not in Sc:
            Dependent+=[v]

    #Categorical variables have discrete values and can't be measured by euclidean distances
    Categorical=['SEX', 'PRIOR.MAL', 'PRIOR.CHEMO', 'PRIOR.XRT', 'Infection', 'cyto.cat', 
                 'ITD', 'D835', 'Ras.Stat', 'resp.simple', 'Relapse', 'vital.status']

    #The last 231 variables are proteins
    Protein=All[-231:]

#Trial_data=Dream9_training[Protein[:4]+Categorical[:4]+['cyto.cat']+Dependent].head()
#Trial_data.T