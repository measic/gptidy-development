### União
uniao_dropnaSliceNome = uniao_dropna['Nome'].str.split(',', expand=True)
uniao_dropna['Primeiro Nome']= uniao_dropnaSliceNome[0]
uniao_dropnaNomeSlice = uniao_dropnaSliceNome[1].str.split('.', expand=True,n=1)
uniao_dropnaComplemntoSlice = uniao_dropnaNomeSlice[1].str.split('(', expand=True)
uniao_dropna['Saudação'] = uniao_dropnaNomeSlice[0]
uniao_dropna['Sobrenome'] = uniao_dropnaComplemntoSlice[0]
uniao_dropna['Complemento'] = uniao_dropnaComplemntoSlice[1]