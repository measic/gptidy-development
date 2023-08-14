### Treino
treinoSliceNome = treino['Nome'].str.split(',', expand=True)
treino['Primeiro Nome']=treinoSliceNome[0]
treinoNomeSlice = treinoSliceNome[1].str.split('.', expand=True,n=1)
treinoComplemntoSlice = treinoNomeSlice[1].str.split('(', expand=True)
treino['Saudação'] = treinoNomeSlice[0]
treino['Sobrenome'] = treinoComplemntoSlice[0]
treino['Complemento'] = treinoComplemntoSlice[1]