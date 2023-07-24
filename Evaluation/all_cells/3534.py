f = open('demographics.txt','r') # open file with reading rights = 'r'

# go through file and trim the new line '\n' at the end
datatxt = [i.splitlines() for i in f.readlines()]

# go through data and split elements in line by tabulators '\t'
datatxt = [i[0].split('\t') for i in datatxt]

f.close() # close file again

for line in datatxt:
    print(line)