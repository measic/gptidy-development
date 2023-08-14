a = RTrunanalysis.loc[RTrunanalysis['Run'] == 2].Invalid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 2].Invalid).tconfint_mean()