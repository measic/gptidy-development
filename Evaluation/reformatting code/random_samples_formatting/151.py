### Treino - DROPNA
treino_dropnaSliceNome = treino_dropna['Nome'].str.split(',', expand=True)
treino_dropna['Primeiro Nome']=treino_dropnaSliceNome[0]
treino_dropnaNomeSlice = treino_dropnaSliceNome[1].str.split('.', expand=True,n=1)
treino_dropnaComplemntoSlice = treino_dropnaNomeSlice[1].str.split('(', expand=True)
treino_dropna['Saudação'] = treino_dropnaNomeSlice[0]
treino_dropna['Sobrenome'] = treino_dropnaComplemntoSlice[0]
treino_dropna['Complemento'] = treino_dropnaComplemntoSlice[1]