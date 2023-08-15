a = RTrunanalysis.loc[RTrunanalysis['Run'] == 3].Invalid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 3].Invalid).tconfint_mean()