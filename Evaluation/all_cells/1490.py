#!/usr/bin/env python
#filename = input('Enter filename: ') #User entered name
filename = 'mystim.txt'  #hard-coded name
idx = 0
trial_time = []
stimulus = []
key = []
with open(filename, 'r') as infile:
    for line in infile:
        first = line[:4]
        last = line[6:]
        if 'TIME' in first:
            trial_time.append(float(last[:5]))
        elif 'STIM' in first:
            stimulus.append(last)
        elif 'KEY ' in first:
            key.append(float(last[0]))
        else:
            #do something here if you want to handle unexpected lines
            pass
        idx +=1

for idx in range(len(key)):
    print("Record",idx)
    print("trial_time {0}  stimulus {1}  key {2}\n".format(trial_time[idx], stimulus[idx], key[idx]))
