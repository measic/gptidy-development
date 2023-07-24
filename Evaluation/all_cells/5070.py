### Colunas de Treino
train=train_csv.copy()
colunasTreino = colunasTeste[:]
colunasTreino.insert(1,'Sobreviventes')
train.columns=colunasTreino