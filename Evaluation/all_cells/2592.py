a = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 1].Invalid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 1].Invalid).tconfint_mean()