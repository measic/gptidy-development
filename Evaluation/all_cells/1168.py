#Calculate how much information in gained on each column
#Calculate the entropy of the subset
def information_gain(Table,Dependent,Independent):
    Table=Table[Table[Dependent].notnull()]
    freq=[]
    for dval in Table[Dependent].unique():
        freq+=[sum(Table[Dependent]==dval)]
    Freq=[float(f)/sum(freq) for f in freq]
    E=0
    for f in Freq:
        E+=-f*np.log(f)/np.log(2)
    #print 'Subset Entropy:', E
    Vars=[]

    #Calculate the entropy of each variable
    for ind in Independent:     
        if ind in Categorical:
            IG=E
            for ival in Table[ind].unique():
                if np.isnan(ival):
                    continue
                SubTable=Table[Table[ind]==ival]
                #print SubTable
                freq=[]
                for dval in Table[Dependent].unique():
                    freq+=[sum(SubTable[Dependent]==dval)]
                Freq=[float(f)/sum(freq) for f in freq]
                #print Freq
                ES=0
                for f in Freq:
                    ES+=-f*np.log(f)/np.log(2) if f<>0 else 0
                #print ES
                IG-=float(len(SubTable))/len(Table)*ES
            #print 'Information gain from %s: %f'%(ind,IG)
            Vars+=[(IG,ind)]
        else:
            Threeshold=[]
            prev_SubTableA_len=0
            for ival in np.arange(min(Table[ind]),max(Table[ind]),(max(Table[ind])-min(Table[ind]))/500.0):
                IG=E
                SubTableA=Table[Table[ind]<ival]
                SubTableB=Table[Table[ind]>=ival]
                if len(SubTableA)<1 or len(SubTableB)<1:
                    continue
                if len(SubTableA)==prev_SubTableA_len:
                    continue
                else:
                    prev_SubTableA_len=len(SubTableA)
                freq=[]
                for dval in Table[Dependent].unique():
                    freq+=[sum(SubTableA[Dependent]==dval)]
                Freq=[float(f)/sum(freq) for f in freq]
                #print Freq
                ES=0
                for f in Freq:
                    ES+=-f*np.log(f)/np.log(2) if f<>0 else 0
                #print ES
                IG-=float(len(SubTableA))/len(Table)*ES
                #print SubTable
                freq=[]
                for dval in Table[Dependent].unique():
                    freq+=[sum(SubTableB[Dependent]==dval)]
                Freq=[float(f)/sum(freq) for f in freq]
                #print Freq
                ES=0
                for f in Freq:
                    ES+=-f*np.log(f)/np.log(2) if f<>0 else 0
                #print ES
                IG-=float(len(SubTableB))/len(Table)*ES
                Threeshold+=[(IG,ival)]
            Threeshold.sort(reverse=True)
            #print Threeshold
            #break
            #print 'Information gain from %s: %f at theeshold:%f'%(ind,Threeshold[0][0],Threeshold[0][1])
            if len(Threeshold)>0:
                Vars+=[(Threeshold[0][0],ind,Threeshold[0][1])]
            else:
                Vars+=[(0,ind)]
    Information_gain=pandas.Series([v[0] for v in Vars],index=[v[1] for v in Vars],name='Information Gain')
    Threesholds=pandas.Series([v[2] for v in Vars if len(v)>2],index=[v[1] for v in Vars if len(v)>2],name='Threeshold')
    return pandas.concat([Information_gain,Threesholds],axis=1)

if __name__=='__main__':
    Q_Cat=['resp.simple','Relapse','vital.status','Overall_Survival_binned','Remission_Duration_binned']
    Ts=[]
    for Variable in Q_Cat:
        print Variable
        Independent=[v for v in Q_training.keys() if v in Q_scoring.keys()]
        Ts+=[information_gain(Q_training,Variable,Independent)]
    Information_Gain=pandas.concat(Ts,keys=Q_Cat,axis=1)
    Information_Gain.to_csv('InformationGain.csv')