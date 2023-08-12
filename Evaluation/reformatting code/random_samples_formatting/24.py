if __name__=='__main__':
    #Correlation for Continuous variables
    Corr=pandas.DataFrame()
    for Variable in Q_Dependent:
        C=Q_training[[t for t in Q_training.keys() if (t not in Q_Dependent)]+[Variable]].corr()[Variable][:-1]
        Corr=Corr.append(C)
    #Write correlation as csv
    Corr.T.to_csv('Correlations.csv')