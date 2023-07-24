import statsmodels.stats.api as sms

#ValidRTCI
a = RTanalysis.Valid.mean()
sms.DescrStatsW(RTanalysis.Valid).tconfint_mean()