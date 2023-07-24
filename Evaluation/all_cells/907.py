#dataframe om alle gediplomeerden in Categorie "Meerdere" te selecteren
df_me = output.loc[output['Categorie'] == 'Meerdere']
df_gme = df_me.groupby(['Gemeente']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_me