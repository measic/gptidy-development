import numpy as np
import xarray as xr
import rasterio
%matplotlib inline
from matplotlib.pyplot import *
from glob import glob
import os
import datetime
import pandas as pd
from rasterio import features
from rasterio_to_xarray import rasterio_to_xarray, xarray_to_rasterio
import rasterstats
import fiona
from tqdm import tqdm
from shapely.geometry import shape
from rasterstats.io import read_features