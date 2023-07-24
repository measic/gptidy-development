gROOT.ProcessLine('.L 16MeVTaMCUnfold_1.cpp')
gROOT.ProcessLine('runMCUnfold()')
gROOT.ProcessLine('HistogramWriter writer')
gROOT.ProcessLine('writer.Th1ToAsciiError(meanResultHisto,"16MeVTa_NSDUnfold_1")')