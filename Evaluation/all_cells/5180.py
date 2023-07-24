treino.loc[(treino['FamiliaQtde']>0),'EstaSozinho']= 0
treino.loc[(treino['FamiliaQtde']==0),'EstaSozinho']= 1

treino_dropna.loc[(treino_dropna['FamiliaQtde']>0),'EstaSozinho']= 0
treino_dropna.loc[(treino_dropna['FamiliaQtde']==0),'EstaSozinho']= 1

teste.loc[(teste['FamiliaQtde']>0),'EstaSozinho']= 0
teste.loc[(teste['FamiliaQtde']==0),'EstaSozinho']= 1

uniao.loc[(uniao['FamiliaQtde']>0),'EstaSozinho']= 0
uniao.loc[(uniao['FamiliaQtde']==0),'EstaSozinho']= 1