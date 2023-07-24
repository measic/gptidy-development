rebin = 0
truncate = {0: 3.365770e-02}#, 1: 2.729744e-01}
outPath = "/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/Unfold/BeamOnly/HEPROW/Inputs/"

gROOT.ProcessLine('HistogramWriter writer;')

for detNum, detName in detNames.iteritems():
    gROOT.ProcessLine('PulseHeightSpectrum{0} = (TH1D*)ops.truncateHist(phs{0}[1],{1},30)'.format(detNum, truncate[detNum]))
    gROOT.ProcessLine('PulseHeightSpectrum{0}->Rebin({1})'.format(detNum, rebin))
    gROOT.ProcessLine('TH1* dataHist{0} = ops.rebinStatistically(PulseHeightSpectrum{0},100);'.format(detNum))
    gROOT.ProcessLine('writer.PhToHEPROW(PulseHeightSpectrum{0},"{1}{2}_phs_03")'.format(detNum, outPath, detName))
    gROOT.ProcessLine('writer.PhToHEPROW(dataHist{0},"{1}{2}_stat_100_phs_03")'.format(detNum, outPath, detName))