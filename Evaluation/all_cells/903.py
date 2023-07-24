#dataframe om alle gediplomeerden in Categorie "Aangrenzend Primair" te selecteren
df_ap = output.loc[output['Categorie'] == 'Aangrenzend Primair']
df_gap = df_ap.groupby(['Gemeente']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_gap