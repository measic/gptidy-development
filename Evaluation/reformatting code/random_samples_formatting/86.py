import os
import sys
mydir = "/Users/pradau/mydata"
filename = "myfile.txt"
pathname = os.path.join(mydir, filename)
if not os.path.isdir(mydir):
    print("Your directory doesn't exist:", mydir)
    sys.exit(1)
if not os.path.isfile(pathname):
    print("Your file doesn't exist at this path:", pathname)
    sys.exit(1)
    
with open(pathname, 'r') as infile:
    for line in infile:
        #print each line of the file regardless of what's in it with prefix (linenumber:)
        # If the text file has line returns at the end of each line, empty lines will be inserted in the print() output.
        print('{}'.format(line))
        