#some error checking we could have used in the earlier lesson
if len(cat) != len(data):
    print('ERROR: Data and categories are not the same length')
    sys.exit(1)  #This means exit with a return code indicating a problem.
else:
    print('No problem with array lengths.')