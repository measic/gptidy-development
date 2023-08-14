gROOT.ProcessLine('DPPBinaryParser parser;')
gROOT.ProcessLine('vector<string> names;')

for filename in os.listdir(path):
    if filename.endswith(".dat"): 
        name = os.path.splitext(filename)[0]
        print "Processing: ", name
        gROOT.ProcessLine('parser.readDatFile("{0}.dat", "{0}.root");'.format(name))
        gROOT.ProcessLine('names.push_back("{0}.root");'.format(name))
        
gROOT.ProcessLine('DDaqPostProcessing obj;')
gROOT.ProcessLine('obj.makePhCalibs(names,"Calibrations_All.root");')