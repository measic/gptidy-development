#dataframe om alle gediplomeerden per provincie te selecteren
df_totaalprovincie = output.groupby(['Provincie']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_totaalprovincie