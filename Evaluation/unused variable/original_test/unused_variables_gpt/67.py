# Plot Resolution function
gROOT.ProcessLine('TF1* resolution = sim0->getResolutionFunction()')
gROOT.ProcessLine('resolution->Draw()')