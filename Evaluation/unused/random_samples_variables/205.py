RTanalysis = pd.DataFrame()
lists = [[] for list in range(0,5)]

for ID in range(10,86):
    sub = cdat[cdat.subject == ID]
    lists[0].append(ID)
    validRT_trials = sub[sub.TrialType == 'Valid'].RT.mean()
    invalidRT_trials = sub[sub.TrialType == 'Invalid'].RT.mean()
    lists[1].append(validRT_trials)
    lists[2].append(invalidRT_trials)
    
RTanalysis['SubjectID'] = lists[0]
RTanalysis['Valid'] = lists[1]
RTanalysis['Invalid'] = lists[2]