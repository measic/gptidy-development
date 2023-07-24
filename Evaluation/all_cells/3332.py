# load data and make some subsets for each wfs for inspection later
dfs = []
for y in [2018, 2019]:
    dfs.append(pd.read_csv(f"../raw_data/{y}_wfs.csv"))
data = pd.concat(dfs)
data['ut'] = pd.to_datetime(data.ut)
data['az'][data['az'] < 0.] += 360.

f9 = data[(data['wfs'] == 'newf9') | (data['wfs'] == 'oldf9')]
f5 = data[data['wfs'] == 'f5']
mmirs = data[data['wfs'] == 'mmirs']
bino = data[data['wfs'] == 'binospec']