%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(0,'../')
from pak import utils
from pak.datasets.MARCOnI import MARCOnI
import matplotlib.pyplot as plt
import itertools

import json; from pprint import pprint
Settings = json.load(open('settings.txt'))
pprint(Settings)

root = Settings['data_root']

marconi = MARCOnI(root)