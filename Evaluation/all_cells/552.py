exclude = ["AmBe", "CalibData"]   #File prefixes for the current calibration run to exclude
tmpName = 'a'
for filename in os.listdir(path):
    name = os.path.splitext(filename)[0]
            
    if filename.endswith(".root") and name.split('_')[1] == runNum \
          and  name.split('_')[0] == "Background":
        print "Adding: ", name
        gROOT.ProcessLine('TFile *{0} = new TFile("{1}.root","update")'.format(tmpName, name))
        gROOT.ProcessLine('eventTree->Draw("m_amplitude>>rebin{0}(1250,0,35000)")'.format(name.split('_')[3]))
        gROOT.ProcessLine('{}->Write()'.format(tmpName)) 
        gROOT.ProcessLine('{}->Close()'.format(tmpName))
        tmpName = chr(ord(tmpName) + 1)
        pause()     
    elif filename.endswith(".root") and name.split('_')[1] == runNum: 
        if name.split('_')[0] not in exclude:
            print "Adding: ", name
            gROOT.ProcessLine('TFile *{0} = new TFile("{1}.root")'.format(tmpName, name))
            gROOT.ProcessLine('eventTree->Draw("m_amplitude>>{0}(1250,0,35000)")'.format(name.split('_')[0]))
            
            gROOT.ProcessLine('TH1F* {0}Data{1} = (TH1F*) {2}->Get("{0}Data")'.format(name.split('_')[0], name.split('_')[3], tmpName))
            gROOT.ProcessLine('{}->cd()'.format(detNames[int(name.split('_')[3])]))
            gROOT.ProcessLine('{}->Write()'.format(name.split('_')[0]))            
            
            gROOT.ProcessLine('{}->Close()'.format(tmpName))
            tmpName = chr(ord(tmpName) + 1)
            pause() 