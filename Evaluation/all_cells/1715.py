import numpy as np
import gdal
import statsmodels.api as sm 
# import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
%matplotlib inline
import seaborn as sns
plt.rcParams["font.sans-serif"] = "Arial"

import pandas as pd
#merged slope raster, accumulation area raster, and watershed raster into one three band raster.
# exported this raster into a text file from OSGeo4W command line:
# gdal2xyz input.tif -band 1 -band 2 -band 3 output.txt. This is a slow operation... 