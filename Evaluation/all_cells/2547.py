AN_sub_RTmeans = cdat.groupby(['subject','RunCounter','TrialType'])['RT'].mean();
AN_sub_ACCmeans = adat.groupby(['subject','RunCounter','TrialType'])['Accuracy'].mean();

#create tidy data csvs
AN_sub_RTmeans.to_csv('SS_ANOVA_RT.csv')
AN_sub_ACCmeans.to_csv('SS_ANOVA_ACC.csv')

#create headers for the tidy data csvs, for analysis purposes
import csv
with open('SS_ANOVA_RT.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('SS_ANOVA_RT.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(["subject", "run", "trialtype", "rt"])
    w.writerows(data)

with open('SS_ANOVA_ACC.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('SS_ANOVA_ACC.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(["subject", "run", "trialtype", "acc"])
    w.writerows(data)