import sys
import os
from ROOT import gROOT

sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/Support'))
from Utilities import pause

path = '/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/CalibData/'
os.chdir(path)
print 'Currently working in: \n {}'.format(os.getcwd())