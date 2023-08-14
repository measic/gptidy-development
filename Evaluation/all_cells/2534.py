sub_RTmeans = cdat.groupby(['subject','TrialType'])['RT'].mean()
RTgrpmean = pd.Series.mean(sub_RTmeans,level=1)
RTgrpmean