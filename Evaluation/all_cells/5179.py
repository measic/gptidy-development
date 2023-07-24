treino['FamiliaQtde'] = treino['ParentesIrmao']+ treino['ParentesFilhos']
treino_dropna['FamiliaQtde'] = treino_dropna['ParentesIrmao']+ treino_dropna['ParentesFilhos']
teste['FamiliaQtde']  = teste['ParentesIrmao']+ teste['ParentesFilhos']
uniao['FamiliaQtde']  = uniao['ParentesIrmao']+ uniao['ParentesFilhos']