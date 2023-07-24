#libraries
#handling data
import pandas as pd
#visualization
from matplotlib import cm
from matplotlib import colors 
import matplotlib.path as mplPath
#operating system
import os
#google maps
from selenium import webdriver
#regexs
import re
import folium
from folium.features import (WmsTileLayer, RegularPolygonMarker, Vega, GeoJson,
                       CircleMarker, LatLngPopup,
                       ClickForMarker, TopoJson, PolyLine, 
                       )
#from progress_bar import log_progress 
import numpy as np
#reading json files
import json
#reading/writing csv files
import csv

from pykml import parser