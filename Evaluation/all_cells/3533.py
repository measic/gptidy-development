f = open('demograhics_new.txt', 'w') # open file with writing rights = 'w'

datatxt_new = [line[1:] for line in datatxt] # delete first column of array

# Go through datatxt array and write each line with specific format to file
for line in datatxt_new:
    f.write("%s\t%s\t%s\n"%(line[0],line[1],line[2]))

f.close() # close file