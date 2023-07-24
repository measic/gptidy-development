### Teste
testeSliceNome = teste['Nome'].str.split(',', expand=True)
teste['Primeiro Nome'] = testeSliceNome[0]
testeNomeSlice = testeSliceNome[1].str.split('.', expand=True, n=1)
testeComplemntoSlice = testeNomeSlice[1].str.split('(', expand=True)
teste['Saudação'] = testeNomeSlice[0]
teste['Sobrenome'] = testeComplemntoSlice[0]
teste['Complemento'] = testeComplemntoSlice[1]