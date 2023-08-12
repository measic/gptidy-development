f = open('demographics.csv','r')   # open the file with reading rights = 'r'
data = [i for i in csv.reader(f) ] # go through file and read each line
f.close()                          # close the file again

for line in data:
    print(line)