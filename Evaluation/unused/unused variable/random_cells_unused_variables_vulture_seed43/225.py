a = RTrunanalysis.loc[RTrunanalysis['Run'] == 0].Invalid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 0].Invalid).tconfint_mean()