#repeat for accuracy

ACCrunanalysis = pd.DataFrame()
new_acclists = [[] for list in range(0,5)]

for ID in range(10,86):
    sub = adat[adat.subject == ID]
    for runID in range(0,4):
        run = sub[sub.RunCounter == runID]
        new_acclists[0].append(ID)
        new_acclists[1].append(runID)
        validACC_trials = run[run.TrialType == 'Valid'].Accuracy.mean()
        invalidACC_trials = run[run.TrialType == 'Invalid'].Accuracy.mean()
        new_acclists[2].append(validACC_trials)
        new_acclists[3].append(invalidACC_trials)
    
ACCrunanalysis['SubjectID'] = new_acclists[0]
ACCrunanalysis['Run'] = new_acclists[1]
ACCrunanalysis['Valid'] = new_acclists[2]
ACCrunanalysis['Invalid'] = new_acclists[3]