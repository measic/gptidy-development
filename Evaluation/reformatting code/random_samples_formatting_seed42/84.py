import os
from ROOT import gROOT

path = '/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/CalibData/'
os.chdir(path)
print 'Currently working in: \n {}'.format(os.getcwd())

gROOT.ProcessLine('.L start33MeVTaCalibration_45.cpp')