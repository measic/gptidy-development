#dataframe om alle gediplomeerden per categorie te selecteren
df_totaalcategorie = output.groupby(['Categorie']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_totaalcategorie