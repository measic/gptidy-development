from os import path, environ
import fiona
import numpy as N
import attitude
from attitude import Orientation, ReconstructedPlane, create_groups
from attitude.display import plot_interactive, init_notebook_mode
from attitude.plot import plot_aligned
from json import dumps
from sys import argv
import palettable as P