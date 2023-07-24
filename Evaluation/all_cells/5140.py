treino['Cabine'] = treino['Cabine'].fillna('SEM_CABINE')
teste['Cabine'] = teste['Cabine'].fillna('SEM_CABINE')
uniao['Cabine'] = uniao['Cabine'].fillna('SEM_CABINE')
uniao.info()