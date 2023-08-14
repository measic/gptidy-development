# import packages
from IPython.display import Markdown, display
from plotly import plotly as py
import qgrid

# import source scripts
import context  # build context to modules in other packages
from data import textfilter
from data.filemgmt import vectorize_docs
from generate_df import DataframeGenerator
from generate_plot import cos_sim_plot, doc_sent_plot, \
    phrase_sent_plot, phrase_sent_scatter, rel_freq_plot, \
    valence_arousal_plot, valence_arousal_dims
from secret import API_KEY, USERNAME
from settings.artistinfo import LINKIN_PARK_ALBUMS