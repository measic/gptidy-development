x = mlb.fit_transform(data['tags'])
df = pd.DataFrame(data=x[1:,0:], columns=mlb.classes_[:])
df.describe()