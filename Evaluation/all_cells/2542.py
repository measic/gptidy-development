#now for run as well

RTrunanalysis = pd.DataFrame()
new_RTlists = [[] for list in range(0,5)]

for ID in range(10,86):
    sub = cdat[cdat.subject == ID]
    for runID in range(0,4):
        run = sub[sub.RunCounter == runID]
        new_RTlists[0].append(ID)
        new_RTlists[1].append(runID)
        validRT_trials = run[run.TrialType == 'Valid'].RT.mean()
        invalidRT_trials = run[run.TrialType == 'Invalid'].RT.mean()
        new_RTlists[2].append(validRT_trials)
        new_RTlists[3].append(invalidRT_trials)
    
RTrunanalysis['SubjectID'] = new_RTlists[0]
RTrunanalysis['Run'] = new_RTlists[1]
RTrunanalysis['Valid'] = new_RTlists[2]
RTrunanalysis['Invalid'] = new_RTlists[3]