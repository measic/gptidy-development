def bin_independent(Table,All_Data,n,name='Binned'):
    Tab=[]
    Thre=[]
    for category in Table:
        #Read the values from all the data
        A=All_Data[category].values.copy()
        #Calculate the threesholds
        A=A[~numpy.isnan(A)]
        A.sort()
        Ts=[]
        for i in range(n):
            Ts+=[A[int(len(A)/float(n)*(i+1))-1]]
        #Make the new Series
        Ser=pandas.Series(Table[category].values.copy()*0,index=Table.index)
        for t in Ts:
            Ser=Ser+(Table[category]<=t)
        Ser.name='%s%i_%s'%(name,n,category)
        Tab+=[Ser]
        Thre+=[pandas.Series(Ts,index=['Threeshold %i'%(i+1) for i in range(len(Ts))],name=category)]
    Threesholds=pandas.concat(Thre,axis=1)
    Threesholds.to_csv('%s%i_Threesholds.csv'%(name,n))
    
    return pandas.concat(Tab,axis=1)

#bin_independent(Trial_data[Protein[:4]],Dream9,2)
#pandas.concat([Trial_data[Protein[:4]],bin_independent(Trial_data[Protein[:4]],Dream9,2),bin_independent(Trial_data[Protein[:4]],Dream9,3)],axis=1).T