treino.loc[treino['Cabine'].notnull(),'TemCabine'] = 1
treino.loc[treino['Cabine']=='SEM_CABINE','TemCabine'] = 0

treino_dropna.loc[treino_dropna['Cabine'].notnull(),'TemCabine'] = 1
treino_dropna.loc[treino_dropna['Cabine']=='SEM_CABINE','TemCabine'] = 0

teste.loc[teste['Cabine'].notnull(),'TemCabine'] = 1
teste.loc[teste['Cabine']=='SEM_CABINE','TemCabine'] = 0

uniao.loc[uniao['Cabine'].notnull(),'TemCabine'] = 1
uniao.loc[uniao['Cabine']=='SEM_CABINE','TemCabine'] = 0