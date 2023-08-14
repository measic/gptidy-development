### Faixa Etárias
treino.loc[(treino['Idade']<1),'FaixaEtaria']=1
treino.loc[(treino['Idade']>=1)  & (treino['Idade']<5),'FaixaEtaria']=2
treino.loc[(treino['Idade']>=5)  & (treino['Idade']<10),'FaixaEtaria']=3
treino.loc[(treino['Idade']>=10) & (treino['Idade']<15),'FaixaEtaria']=4
treino.loc[(treino['Idade']>=15) & (treino['Idade']<20),'FaixaEtaria']=5
treino.loc[(treino['Idade']>=20) & (treino['Idade']<25),'FaixaEtaria']=6
treino.loc[(treino['Idade']>=25) & (treino['Idade']<30),'FaixaEtaria']=7
treino.loc[(treino['Idade']>=30) & (treino['Idade']<35),'FaixaEtaria']=8
treino.loc[(treino['Idade']>=35) & (treino['Idade']<40),'FaixaEtaria']=9
treino.loc[(treino['Idade']>=40) & (treino['Idade']<45),'FaixaEtaria']=10
treino.loc[(treino['Idade']>=45) & (treino['Idade']<50),'FaixaEtaria']=11
treino.loc[(treino['Idade']>=50) & (treino['Idade']<55),'FaixaEtaria']=12
treino.loc[(treino['Idade']>=55) & (treino['Idade']<60),'FaixaEtaria']=13
treino.loc[(treino['Idade']>=60) & (treino['Idade']<65),'FaixaEtaria']=14
treino.loc[(treino['Idade']>=65) & (treino['Idade']<70),'FaixaEtaria']=15
treino.loc[(treino['Idade']>=70) & (treino['Idade']<75),'FaixaEtaria']=16
treino.loc[(treino['Idade']>=75) & (treino['Idade']<80),'FaixaEtaria']=17
treino.loc[(treino['Idade']>=80),'FaixaEtaria']=18

treino_dropna.loc[(treino_dropna['Idade']<1),'FaixaEtaria']=1
treino_dropna.loc[(treino_dropna['Idade']>=1)  & (treino_dropna['Idade']<5),'FaixaEtaria']=2
treino_dropna.loc[(treino_dropna['Idade']>=5)  & (treino_dropna['Idade']<10),'FaixaEtaria']=3
treino_dropna.loc[(treino_dropna['Idade']>=10) & (treino_dropna['Idade']<15),'FaixaEtaria']=4
treino_dropna.loc[(treino_dropna['Idade']>=15) & (treino_dropna['Idade']<20),'FaixaEtaria']=5
treino_dropna.loc[(treino_dropna['Idade']>=20) & (treino_dropna['Idade']<25),'FaixaEtaria']=6
treino_dropna.loc[(treino_dropna['Idade']>=25) & (treino_dropna['Idade']<30),'FaixaEtaria']=7
treino_dropna.loc[(treino_dropna['Idade']>=30) & (treino_dropna['Idade']<35),'FaixaEtaria']=8
treino_dropna.loc[(treino_dropna['Idade']>=35) & (treino_dropna['Idade']<40),'FaixaEtaria']=9
treino_dropna.loc[(treino_dropna['Idade']>=40) & (treino_dropna['Idade']<45),'FaixaEtaria']=10
treino_dropna.loc[(treino_dropna['Idade']>=45) & (treino_dropna['Idade']<50),'FaixaEtaria']=11
treino_dropna.loc[(treino_dropna['Idade']>=50) & (treino_dropna['Idade']<55),'FaixaEtaria']=12
treino_dropna.loc[(treino_dropna['Idade']>=55) & (treino_dropna['Idade']<60),'FaixaEtaria']=13
treino_dropna.loc[(treino_dropna['Idade']>=60) & (treino_dropna['Idade']<65),'FaixaEtaria']=14
treino_dropna.loc[(treino_dropna['Idade']>=65) & (treino_dropna['Idade']<70),'FaixaEtaria']=15
treino_dropna.loc[(treino_dropna['Idade']>=70) & (treino_dropna['Idade']<75),'FaixaEtaria']=16
treino_dropna.loc[(treino_dropna['Idade']>=75) & (treino_dropna['Idade']<80),'FaixaEtaria']=17
treino_dropna.loc[(treino_dropna['Idade']>=80),'FaixaEtaria']=18

teste.loc[(teste['Idade']<1),'FaixaEtaria']=1
teste.loc[(teste['Idade']>=1)  & (teste['Idade']<5),'FaixaEtaria']=2
teste.loc[(teste['Idade']>=5)  & (teste['Idade']<10),'FaixaEtaria']=3
teste.loc[(teste['Idade']>=10) & (teste['Idade']<15),'FaixaEtaria']=4
teste.loc[(teste['Idade']>=15) & (teste['Idade']<20),'FaixaEtaria']=5
teste.loc[(teste['Idade']>=20) & (teste['Idade']<25),'FaixaEtaria']=6
teste.loc[(teste['Idade']>=25) & (teste['Idade']<30),'FaixaEtaria']=7
teste.loc[(teste['Idade']>=30) & (teste['Idade']<35),'FaixaEtaria']=8
teste.loc[(teste['Idade']>=35) & (teste['Idade']<40),'FaixaEtaria']=9
teste.loc[(teste['Idade']>=40) & (teste['Idade']<45),'FaixaEtaria']=10
teste.loc[(teste['Idade']>=45) & (teste['Idade']<50),'FaixaEtaria']=11
teste.loc[(teste['Idade']>=50) & (teste['Idade']<55),'FaixaEtaria']=12
teste.loc[(teste['Idade']>=55) & (teste['Idade']<60),'FaixaEtaria']=13
teste.loc[(teste['Idade']>=60) & (teste['Idade']<65),'FaixaEtaria']=14
teste.loc[(teste['Idade']>=65) & (teste['Idade']<70),'FaixaEtaria']=15
teste.loc[(teste['Idade']>=70) & (teste['Idade']<75),'FaixaEtaria']=16
teste.loc[(teste['Idade']>=75) & (teste['Idade']<80),'FaixaEtaria']=17
teste.loc[(teste['Idade']>=80),'FaixaEtaria']=18

uniao.loc[(uniao['Idade']<1),'FaixaEtaria']=1
uniao.loc[(uniao['Idade']>=1)  & (uniao['Idade']<5),'FaixaEtaria']=2
uniao.loc[(uniao['Idade']>=5)  & (uniao['Idade']<10),'FaixaEtaria']=3
uniao.loc[(uniao['Idade']>=10) & (uniao['Idade']<15),'FaixaEtaria']=4
uniao.loc[(uniao['Idade']>=15) & (uniao['Idade']<20),'FaixaEtaria']=5
uniao.loc[(uniao['Idade']>=20) & (uniao['Idade']<25),'FaixaEtaria']=6
uniao.loc[(uniao['Idade']>=25) & (uniao['Idade']<30),'FaixaEtaria']=7
uniao.loc[(uniao['Idade']>=30) & (uniao['Idade']<35),'FaixaEtaria']=8
uniao.loc[(uniao['Idade']>=35) & (uniao['Idade']<40),'FaixaEtaria']=9
uniao.loc[(uniao['Idade']>=40) & (uniao['Idade']<45),'FaixaEtaria']=10
uniao.loc[(uniao['Idade']>=45) & (uniao['Idade']<50),'FaixaEtaria']=11
uniao.loc[(uniao['Idade']>=50) & (uniao['Idade']<55),'FaixaEtaria']=12
uniao.loc[(uniao['Idade']>=55) & (uniao['Idade']<60),'FaixaEtaria']=13
uniao.loc[(uniao['Idade']>=60) & (uniao['Idade']<65),'FaixaEtaria']=14
uniao.loc[(uniao['Idade']>=65) & (uniao['Idade']<70),'FaixaEtaria']=15
uniao.loc[(uniao['Idade']>=70) & (uniao['Idade']<75),'FaixaEtaria']=16
uniao.loc[(uniao['Idade']>=75) & (uniao['Idade']<80),'FaixaEtaria']=17
uniao.loc[(uniao['Idade']>=80),'FaixaEtaria']=18