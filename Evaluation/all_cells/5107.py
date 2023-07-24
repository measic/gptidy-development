### Resposta: Não
df_mesma_cabine = pd.DataFrame({'Sobreviventes':mesma_cabine.index.get_level_values(0),'Cabine':mesma_cabine.index.get_level_values(1), 'CabineQuantidade':mesma_cabine.values})
df_mesma_cabine.groupby(['Sobreviventes','CabineQuantidade']).size()