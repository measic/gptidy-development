a = RTrunanalysis.loc[RTrunanalysis['Run'] == 1].Valid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 1].Valid).tconfint_mean()