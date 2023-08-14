a = RTrunanalysis.loc[RTrunanalysis['Run'] == 1].Invalid.mean()
sms.DescrStatsW(RTrunanalysis.loc[RTrunanalysis['Run'] == 1].Invalid).tconfint_mean()