### Resposta: Não
df_mesmo_numero_passagem = pd.DataFrame({'Sobreviventes':mesmo_numero_passagem.index.get_level_values(0),'Passagem':mesmo_numero_passagem.index.get_level_values(1), 'PassagemQuantidade':mesmo_numero_passagem.values})
df_mesmo_numero_passagem.groupby(['Sobreviventes','PassagemQuantidade']).size()