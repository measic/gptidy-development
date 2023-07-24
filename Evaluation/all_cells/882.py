# Creeer dataframe met daarin het aantal behaalde diploma's per kwalificatie #BK
df_totaalKN = df.groupby(['KWALIFICATIE NAAM']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_totaalKN.head()