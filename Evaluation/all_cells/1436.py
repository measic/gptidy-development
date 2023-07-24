import scipy.io as sio
import os
import matplotlib.pyplot as plt
import numpy as np

#squeeze_me will turn the single column 2D matrix into a single row vector.
mat_contents = sio.loadmat( 'matlab_exercises' + os.sep + 'lesson2.mat', squeeze_me=True)
data = mat_contents['data']
print(data)