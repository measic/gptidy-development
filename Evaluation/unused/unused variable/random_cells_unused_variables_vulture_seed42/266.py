a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 3].Valid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 3].Valid).tconfint_mean()