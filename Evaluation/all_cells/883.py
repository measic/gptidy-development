# Top 10 meest behaalde diploma's jaar 2017 - Wervingsgebied Zwolle # BK

df_zwolle = df
df_zwolle = df_zwolle.loc[df_zwolle['Locatie'] == 'Zwolle']
df_zwolle = df_zwolle.groupby(['KWALIFICATIE NAAM','MBO SECTOR']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_zwolle = df_zwolle.sort_values(by='2017   AANT', ascending=False)
# Laat de (10) meest voorkomende diploma's zien van 2017
df_zwolle10 = df_zwolle.nlargest(10, '2017   AANT')
df_zwolle10

# Opleiding Mbo-Verpleegkundige lijkt enorm gegroeid te zijn, maar werd eerder als MBO-verpleegkundige omschreven.