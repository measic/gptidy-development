treino['SaudacaoNum'] = treino['Saudação'].replace(saudacoes,quantidadesSaudacoes)
treino_dropna['SaudacaoNum'] = treino_dropna['Saudação'].replace(saudacoes,quantidadesSaudacoes)
teste['SaudacaoNum'] = teste['Saudação'].replace(saudacoes,quantidadesSaudacoes)
uniao['SaudacaoNum'] = uniao['Saudação'].replace(saudacoes,quantidadesSaudacoes)
uniao_dropna['SaudacaoNum'] = uniao_dropna['Saudação'].replace(saudacoes,quantidadesSaudacoes)
uniao.info()