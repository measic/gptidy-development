import pandas as pd
from bokeh.models.glyphs import Circle
from bokeh.plotting import show, output_notebook,figure
from bokeh.models import (
    GMapPlot, GMapOptions, Range1d, ColumnDataSource, LinearAxis,
    PanTool, WheelZoomTool,HoverTool, TapTool, OpenURL)
output_notebook()