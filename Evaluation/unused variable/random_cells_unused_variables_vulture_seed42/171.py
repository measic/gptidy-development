detNames = {0: 'Det0'}  ###REMOVE WHEN YOU GET ACTUAL PSD CUTS ON THEM ALL!

gROOT.ProcessLine('HistogramOperations ops')
gROOT.ProcessLine('lightTables.setBirksParams(1.0,6.90)')

for detNum, detName in detNames.iteritems():
    params = CalibParams(calPath+calNames[detNum])
    gROOT.ProcessLine('vector<TH1*> phs{1} = ops.loadHistograms("33MeVTa_{0}_ls_{1}_fittedPSDCut.root")'.format(runNum,detNum))
    gROOT.ProcessLine('ops.applyCalibration(phs{0}[1],{1},{2})'.format(detNum, params.a, params.b))
    gROOT.ProcessLine('TFile *tgt{0} = new TFile("33MeVTa_{0}_ls_{1}_calibFittedPSDCut.root","recreate")'.format(runNum,detNum))
    gROOT.ProcessLine('phs{0}[1]->Rebin(3)'.format(detNum))
    gROOT.ProcessLine('phs{0}[1]->Draw()'.format(detNum))    
    gROOT.ProcessLine('phs{0}[1]->Write()'.format(str(detNum)))
    pause()