import time
import os
import importlib

# path = 'C:/Users/lingyu.yue/Documents/Xiao_Fan/GAN'
path="/Users/louis/Google Drive/M.Sc-DIRO-UdeM/IFT6135-Apprentissage de représentations/assignment4/"
if os.path.isdir(path):
    os.chdir(path)
else:
    os.chdir("./")
print(os.getcwd())

import matplotlib.pyplot as plt
from scipy.misc import imresize
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from torchvision.utils import save_image
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from PIL import Image
import itertools
import inception_score 
import GAN_CelebA
#from GAN_train import loadCheckpoint,generator,generator_Upsampling,discriminator,show_result
importlib.reload(GAN_CelebA)
importlib.reload(inception_score)

use_cuda = torch.cuda.is_available()
torch.manual_seed(999)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(999)
