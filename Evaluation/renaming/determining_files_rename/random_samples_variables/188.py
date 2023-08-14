variable_def = pd.DataFrame()
new_RTlists = [[] for list in range(0, 5)]
for ID in range(10, 86):
    sub = cdat[cdat.subject == ID]
    for runID in range(0, 4):
        run = sub[sub.RunCounter == runID]
        new_RTlists[0].append(ID)
        new_RTlists[1].append(runID)
        validRT_trials = run[run.TrialType == 'Valid'].RT.mean()
        invalidRT_trials = run[run.TrialType == 'Invalid'].RT.mean()
        new_RTlists[2].append(validRT_trials)
        new_RTlists[3].append(invalidRT_trials)
variable_def['SubjectID'] = new_RTlists[0]
variable_def['Run'] = new_RTlists[1]
variable_def['Valid'] = new_RTlists[2]
variable_def['Invalid'] = new_RTlists[3]