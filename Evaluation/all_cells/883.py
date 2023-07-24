# Top 10 meest behaalde diploma's jaar 2017 - Landelijk #BK

df_landelijk = df.groupby(['KWALIFICATIE NAAM','MBO SECTOR']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_landelijk = df_landelijk.sort_values(by='2017   AANT', ascending=False)
# Laat de (10) meest voorkomende diploma's van 2017 zien
df_landelijk10 = df_landelijk.nlargest(10, '2017   AANT')
df_landelijk10