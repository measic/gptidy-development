for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('AmBe{}->cd()'.format(detNum))
    gROOT.ProcessLine('eventTree->Draw("m_amplitude>>AmBeGamma(1250,0,35000)","(m_amplitude-m_shape)/m_shape<{}")'.format(cutPt[detNum]))
    gROOT.ProcessLine('TH1F* AmBeData{0} = (TH1F*) AmBe{0}->Get("AmBeGamma")'.format(detNum))
    gROOT.ProcessLine('AmBe{0}->Write()'.format(detNum))
    pause()
    
    gROOT.ProcessLine('{0}->cd()'.format(detName))
    gROOT.ProcessLine('AmBeData{}->Write()'.format(detNum))
    gROOT.ProcessLine('AmBe{}->Close()'.format(detNum))