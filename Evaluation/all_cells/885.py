#dataframe om alle gediplomeerden in regio Flevoland te selecteren
df_locatie_flevoland = df.loc[df['Locatie'] == 'Flevoland']
df_aantal_flevoland = df_locatie_flevoland.groupby(['Locatie']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]