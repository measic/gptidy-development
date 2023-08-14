if __name__=='__main__':
    #Most important Variables in Correlation
    for Variable in Q_Dependent:
        A=Corr.T[Variable]**2
        A.sort(ascending=False)
        print Corr[A.head(10).index].T[Variable]