treino['Complemento'] = treino['Complemento'].fillna('NAO_INFORMADO')
treino_dropna['Complemento'] = treino_dropna['Complemento'].fillna('NAO_INFORMADO')
teste['Complemento'] = teste['Complemento'].fillna('NAO_INFORMADO')
uniao['Complemento'] = uniao['Complemento'].fillna('NAO_INFORMADO')
uniao_dropna['Complemento'] = uniao_dropna['Complemento'].fillna('NAO_INFORMADO')
uniao.info()