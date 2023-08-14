a = RTrunanalysis.loc[RTrunanalysis['Run'] == 3].Valid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 3].Valid).tconfint_mean()