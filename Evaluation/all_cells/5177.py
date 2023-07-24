#Sexo
treino['SexoNum']        = treino['Sexo'].replace(['male','female'],[1,0])
treino_dropna['SexoNum'] = treino_dropna['Sexo'].replace(['male','female'],[1,0])
teste['SexoNum']         = teste['Sexo'].replace(['male','female'],[1,0])
uniao['SexoNum']         = uniao['Sexo'].replace(['male','female'],[1,0])
uniao_dropna['SexoNum']  = uniao_dropna['Sexo'].replace(['male','female'],[1,0])
treino.head(2)