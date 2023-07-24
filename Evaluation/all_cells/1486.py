#read myfile by getting file handle 'infile' with a context manager.
idx = 0
with open('myfile.txt', 'r') as infile:
    for line in infile:
        #print each line of the file regardless of what's in it with prefix (linenumber:)
        # If the text file has line returns at the end of each line, empty lines will be inserted in the print() output.
        print('{0}:{1}'.format(idx,line))
        idx +=1
        