import statsmodels.stats.api as sms

#ValidRTCI
RTanalysis.Valid.mean()
sms.DescrStatsW(RTanalysis.Valid).tconfint_mean()