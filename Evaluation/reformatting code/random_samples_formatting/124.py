from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=4, random_state=0)
regr.fit(x,y)
### Quanto maior o score, maior a importância do atributo
print(colunasNumericasIdade)
print(regr.feature_importances_)