# Top 10 meest behaalde diploma's jaar 2017 - Wervingsgebied Flevoland # BK

df_flevoland = df
df_flevoland = df_flevoland.loc[df_flevoland['Locatie'] == 'Flevoland']
df_flevoland = df_flevoland.groupby(['KWALIFICATIE NAAM','MBO SECTOR']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_flevoland = df_flevoland.sort_values(by='2017   AANT', ascending=False)
# Laat de (10) meest voorkomende diploma's van 2017 zien
df_flevoland10 = df_flevoland.nlargest(10, '2017   AANT')
df_flevoland10

# Opleiding Mbo-Verpleegkundige lijkt enorm gegroeid te zijn, maar werd eerder als MBO-verpleegkundige omschreven.