driftSrc = 'AmBe'
runNums = ['002', '003']
colorWheel = ['kGreen', 'kBlue']

gROOT.ProcessLine('TFile f("Calibrations_All.root")')
gROOT.ProcessLine('TLine* line = new TLine(0,1,7000,1)')

for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('TCanvas c{}'.format(detNum))
    for run, color in zip(runNums, colorWheel):
        gROOT.ProcessLine('TH1* {0}_{1} = (TH1*) f.Get("{2}_{1}_ls_{3}.root")->Clone()'.format(detName, run, driftSrc, detNum))
        gROOT.ProcessLine('{0}_{1}->Scale(1.0/{0}_{1}->Integral())'.format(detName, run))
        gROOT.ProcessLine('{0}_{1}->Rebin(2)'.format(detName, run))
        gROOT.ProcessLine('{0}_{1}->SetLineColor({2})'.format(detName, run, color))
        gROOT.ProcessLine('{0}_{1}->Draw("same")'.format(detName, run))
        
    gROOT.ProcessLine('TH1* postToPreRatio{0} = (TH1*){0}_{1}->Clone()'.format(detName, runNums[-1]))
    gROOT.ProcessLine('postToPreRatio{0}->Divide({0}_{1})'.format(detName, runNums[-2]))
    gROOT.ProcessLine('TCanvas c{}'.format(detName))
    gROOT.ProcessLine('postToPreRatio{0}->Draw()'.format(detName))
    gROOT.ProcessLine('line->Draw("same")')
    pause()