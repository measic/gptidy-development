ACCrunanalysis = pd.DataFrame()
variable_def = [[] for list in range(0, 5)]
for ID in range(10, 86):
    sub = adat[adat.subject == ID]
    for runID in range(0, 4):
        run = sub[sub.RunCounter == runID]
        variable_def[0].append(ID)
        variable_def[1].append(runID)
        validACC_trials = run[run.TrialType == 'Valid'].Accuracy.mean()
        invalidACC_trials = run[run.TrialType == 'Invalid'].Accuracy.mean()
        variable_def[2].append(validACC_trials)
        variable_def[3].append(invalidACC_trials)
ACCrunanalysis['SubjectID'] = variable_def[0]
ACCrunanalysis['Run'] = variable_def[1]
ACCrunanalysis['Valid'] = variable_def[2]
ACCrunanalysis['Invalid'] = variable_def[3]