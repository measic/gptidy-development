RTanalysis = pd.DataFrame()
variable_def = [[] for list in range(0, 5)]
for ID in range(10, 86):
    sub = cdat[cdat.subject == ID]
    variable_def[0].append(ID)
    validRT_trials = sub[sub.TrialType == 'Valid'].RT.mean()
    invalidRT_trials = sub[sub.TrialType == 'Invalid'].RT.mean()
    variable_def[1].append(validRT_trials)
    variable_def[2].append(invalidRT_trials)
RTanalysis['SubjectID'] = variable_def[0]
RTanalysis['Valid'] = variable_def[1]
RTanalysis['Invalid'] = variable_def[2]