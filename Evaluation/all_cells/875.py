#dataframe om alle gediplomeerden in regio Zwolle te selecteren
df_locatie_zwolle = df.loc[df['Locatie'] == 'Zwolle']
df_aantal_zwolle = df_locatie_zwolle.groupby(['Locatie']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]