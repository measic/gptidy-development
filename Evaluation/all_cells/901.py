#dataframe om alle gediplomeerden in Categorie "Thuismarkt" te selecteren
df_thuismarkt = output.loc[output['Categorie'] == 'Thuismarkt']
df_gt = df_thuismarkt.groupby(['Gemeente']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_gt