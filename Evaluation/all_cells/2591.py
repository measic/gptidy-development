a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 2].Valid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 2].Valid).tconfint_mean()