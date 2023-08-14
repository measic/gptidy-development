cutPt={0: 0.28, 2: 0.3, 4:0.29}
for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('AmBe{}->cd()'.format(detNum))
    #gROOT.ProcessLine('eventTree->Draw("(m_amplitude-m_shape)/m_shape:m_shape>>(1250,0,35000,1024,0,1)","(m_amplitude-m_shape)/m_amplitude<{}","colz")'.format(cutPt[detNum]))
    pause()