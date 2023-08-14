a = RTrunanalysis.loc[RTrunanalysis['Run'] == 0].Valid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 0].Valid).tconfint_mean()