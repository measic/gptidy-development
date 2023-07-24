a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 0].Invalid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 0].Invalid).tconfint_mean()