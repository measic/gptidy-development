a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 0].Valid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 0].Valid).tconfint_mean()