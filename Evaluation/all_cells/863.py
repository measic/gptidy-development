import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

from seaborn import countplot
from matplotlib.pyplot import figure, show

from bokeh.io import show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.models import FactorRange
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models.widgets import CheckboxGroup
from bokeh.layouts import column, row, WidgetBox

host = "mysql.nm-interactive.net"
port = 3306
user = "windesheim"
password = "pMjq357Kdee7Sx8C"
database = "windesheim"
client = "mysql"

#Installeer eerst Mysqlcient in Anaconda Navigator
engine = create_engine("{0}://{1}:{2}@{3}:{4}/{5}".format(client, user, password, host, port, database))

datasource = pd.read_sql_query("SELECT * FROM source WHERE KWALIFICATIENIVEAU = 4",engine)
wervingsgebieden = pd.read_sql_query("SELECT * FROM wervingsgebieden",engine)
datasource.info()
wervingsgebieden.info()