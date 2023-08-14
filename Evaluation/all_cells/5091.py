#Valor total - bruto: 891
#Valor total - Sem Nulos: 712
train_dropna=train.dropna(subset=colunasSemCabine)
train_dropna.describe()