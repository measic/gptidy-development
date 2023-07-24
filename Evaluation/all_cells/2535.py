adat['TrialType'] = adat['Valid'].isin([1])
adat.loc[adat['Valid'].isin([1]), 'TrialType'] = 'Valid'
adat.loc[~adat['Valid'].isin([1]), 'TrialType'] = 'Invalid'

cdat['TrialType'] = cdat['Valid'].isin([1])
cdat.loc[cdat['Valid'].isin([1]), 'TrialType'] = 'Valid'
cdat.loc[~cdat['Valid'].isin([1]), 'TrialType'] = 'Invalid'