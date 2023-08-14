# Close all of the files
for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('{}->Close()'.format(detName))