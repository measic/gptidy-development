# Set file characteristics
runNum = "003"

# Initialize storage        
# Plot each PSD
for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('TFile *AmBe{0} = new TFile("AmBe_{1}_ls_{0}.root","update")'.format(detNum,runNum))
    #gROOT.ProcessLine('eventTree->Draw("(m_amplitude-m_shape)/m_shape:m_shape>>(1250,0,35000,1024,0,1)","","colz")')
    
    gROOT.ProcessLine('TFile *{0} = new TFile("CalibData_{1}.root","recreate")'.format(detName, detNum))
    pause()