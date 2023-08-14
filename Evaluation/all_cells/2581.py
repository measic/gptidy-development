a = RTrunanalysis.loc[RTrunanalysis['Run'] == 2].Valid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 2].Valid).tconfint_mean()