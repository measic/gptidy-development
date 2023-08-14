#Define types of variables

Protein=list(Q_training.keys()[27:27+231])
Categorical=['SEX', 'PRIOR.MAL', 'PRIOR.CHEMO', 'PRIOR.XRT', 'Infection', 
             'ITD', 'D835', 'Ras.Stat', 'resp.simple', 'Relapse', 'vital.status'] + list(Q_training.keys()[269:283])
Dependent=[v for v in Q_training.keys() if v not in Q_scoring.keys()]
Q_Dependent=Dependent #Temp
Protein_Squared=list(Q_training.keys()[283:283+231])
Protein_Absolute=list(Q_training.keys()[514:514+231])
Protein_Binned2=list(Q_training.keys()[745:745+231])
Protein_Binned3=list(Q_training.keys()[976:976+231])
Protein_Binned4=list(Q_training.keys()[1207:1207+231])
Protein_Binned5=list(Q_training.keys()[1438:1438+231])
Protein_PCA=list(Q_training.keys()[1669:1669+200])
Protein_PCAWhiten=list(Q_training.keys()[1869:1869+200])
Protein_PCASq=list(Q_training.keys()[2069:2069+200])
Original=list(Q_training.keys()[:283])
