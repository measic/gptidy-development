#dataframe om alle gediplomeerden in Categorie "Aangrenzend Secundair" te selecteren
df_as = output.loc[output['Categorie'] == 'Aangrenzend Secundair']
df_gas = df_as.groupby(['Gemeente']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_gas