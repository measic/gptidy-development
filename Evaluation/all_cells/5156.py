### União
uniaoSliceNome = uniao['Nome'].str.split(',', expand=True)
uniao['Primeiro Nome']=uniaoSliceNome[0]
uniaoNomeSlice = uniaoSliceNome[1].str.split('.', expand=True,n=1)
uniaoComplemntoSlice = uniaoNomeSlice[1].str.split('(', expand=True)
uniao['Saudação'] = uniaoNomeSlice[0]
uniao['Sobrenome'] = uniaoComplemntoSlice[0]
uniao['Complemento'] = uniaoComplemntoSlice[1]