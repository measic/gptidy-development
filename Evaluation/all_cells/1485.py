#read myfile without a context manager.
idx = 0
infile = open('myfile.txt', 'r')
for line in infile:
    #print each line of the file regardless of what's in it with prefix (linenumber:)
    # If the text file has line returns at the end of each line, which inserts empty lines in the print() output.
    print('{0}:{1}'.format(idx,line))
    idx +=1
infile.close()