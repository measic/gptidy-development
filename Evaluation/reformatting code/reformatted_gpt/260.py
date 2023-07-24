import pandas as pd

ACCanalysis = pd.DataFrame()
new_lists = [[] for _ in range(0, 5)]

for ID in range(10, 86):
    sub = adat[adat.subject == ID]
    new_lists[0].append(ID)
    validACC_trials = sub[sub.TrialType == 'Valid'].Accuracy.mean()
    invalidACC_trials = sub[sub.TrialType == 'Invalid'].Accuracy.mean()
    new_lists[1].append(validACC_trials)
    new_lists[2].append(invalidACC_trials)

ACCanalysis['SubjectID'] = new_lists[0]
ACCanalysis['Valid'] = new_lists[1]
ACCanalysis['Invalid'] = new_lists[2]