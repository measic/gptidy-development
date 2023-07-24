colunasNumericas=['Classe','ParentesIrmao','ParentesFilhos','Idade','PassagemPreco']
x = pd.DataFrame(train_dropna,columns=colunasNumericas).values
y = train_dropna['Sobreviventes']