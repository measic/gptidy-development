variable_def = ACCrunanalysis.loc[ACCrunanalysis['Run'] == 2].Invalid.mean()
sms.DescrStatsW(ACCrunanalysis.loc[ACCrunanalysis['Run'] == 2].Invalid).tconfint_mean()