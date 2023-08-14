a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 1].Valid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 1].Valid).tconfint_mean()