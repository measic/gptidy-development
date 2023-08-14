import datetime

import numpy as np
import pandas as pd
from ics import Calendar

import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly import tools
import cufflinks as cf

from lib.custom_utils import generate_wordcloud, get_semester_date_range, get_semester_asana, get_semester_via_col

init_notebook_mode(connected=True)
cf.set_config_file(world_readable=True, offline=True)