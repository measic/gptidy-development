sub_ACCmeans = adat.groupby(['subject','TrialType'])['Accuracy'].mean()
ACCgrpmean = pd.Series.mean(sub_ACCmeans,level=1)
ACCgrpmean