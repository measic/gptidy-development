RTanalysis = pd.DataFrame()
lists = [[] for list in range(0, 5)]
for ID in range(10, 86):
    sub = cdat[cdat.subject == ID]
    lists[0].append(ID)
    validRT_trials = sub[sub.TrialType == 'Valid'].RT.mean()
    variable_def = sub[sub.TrialType == 'Invalid'].RT.mean()
    lists[1].append(validRT_trials)
    lists[2].append(variable_def)
RTanalysis['SubjectID'] = lists[0]
RTanalysis['Valid'] = lists[1]
RTanalysis['Invalid'] = lists[2]