colunasNumericasIdade=['Classe','ParentesIrmao','ParentesFilhos','SaudacaoNum','PassagemPreco']
x = pd.DataFrame(treino_dropna,columns=colunasNumericasIdade).values
y = treino_dropna['Idade'].astype('float32')