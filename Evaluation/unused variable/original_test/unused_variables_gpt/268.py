')
from virtual_stations import get_waterlevel
from misc import get_precipitation, get_pet, get_label_tree, startswith_label, get_mask, get_masks, str2datetime, get_peq_from_df, gcs_get_dir
from models import gr4hh
from mcmc_utils import dist_map, get_likelihood_logp, get_prior_logp

from mcmc import smc, dist
from datetime import timedelta
import random
import subprocess
import pickle
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
from tqdm import tqdm
import xarray as xr
import gcsfs
from dask.distributed import Client

is_pangeo_data = False # True if in Pangeo binder, False if in laptop
if is_pangeo_data:
    from dask_kubernetes import KubeCluster as Cluster
    n_workers = 10
else:
    from dask.distributed import LocalCluster as Cluster
    n_workers = 4

%matplotlib inline
import matplotlib.pyplot as plt