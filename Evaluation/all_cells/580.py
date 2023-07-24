import os
import sys
from ROOT import gROOT
import numpy as np

sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/Support'))
sys.path.insert(0,os.path.abspath('/home/pyne-user/Dropbox/UCB/Computational_Tools/Scripts/Python/Unfolding'))
from Utilities import pause
from Root import CalibParams

outPath = "/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/Unfold/BeamOnly/HEPROW/Inputs/"
rspPath= '/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Simulated/PHS/ResponseMatrices/simSideResponse20Mil.root'
calPath = '/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/CalibData/'

os.chdir(outPath)
print 'Currently working in: \n {}'.format(os.getcwd())

detNames = {0: 'Det0'}#, 2: 'Det45', 4: 'Det90'}
calNames = {0: 'CalibParams_0.txt'}#, 2: 'CalibParams_2.txt', 4: 'CalibParams_4.txt'}