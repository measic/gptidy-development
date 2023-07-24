gROOT.ProcessLine('DPPBinaryParser parser;')

for filename in os.listdir(path):
    if filename.endswith(".dat"): 
        name = os.path.splitext(filename)[0]
        print 'Processing: ', filename
        gROOT.ProcessLine('parser.readDatFile("{0}.dat", "{0}.root", true);'.format(name))