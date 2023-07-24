colunasNumericasIdade = ['Classe', 'Idade', 'FaixaEtaria', 'ParentesIrmao', 'ParentesFilhos', 'SaudacaoNum', 'PassagemPreco', 'SexoNum', 'PortoEmbarqueNum', 'FamiliaQtde', 'EstaSozinho', 'TemCabine']
x = pd.DataFrame(treino_dropna, columns=colunasNumericasIdade).values
y = treino_dropna['Idade'].astype('float32')