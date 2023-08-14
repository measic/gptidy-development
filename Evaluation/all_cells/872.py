df_totaalSBB = df.groupby(['SECTORUNIT SBB']).sum()[['2013   AANT','2014   AANT','2015   AANT','2016   AANT','2017   AANT']]
df_totaalSBB.info()