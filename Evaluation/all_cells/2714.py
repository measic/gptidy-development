import h2o
import numpy as np
import math
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch
h2o.init(nthreads=-1, strict_version_check=True)
## optional: connect to a running H2O cluster
#h2o.init(ip="mycluster", port=55555)