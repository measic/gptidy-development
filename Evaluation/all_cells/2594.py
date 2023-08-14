a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 3].Invalid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 3].Invalid).tconfint_mean()