with open('demographics.txt','r') as f:

    datatxt = [i.splitlines() for i in f.readlines()]
    datatxt = [i[0].split('\t') for i in datatxt]

for line in datatxt:
    print(line)