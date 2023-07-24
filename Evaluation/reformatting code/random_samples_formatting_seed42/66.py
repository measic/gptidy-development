from gensim.models import Word2Vec
import pandas as pd
import pickle
import time
import logging
import multiprocessing as mp
import os
logging.basicConfig(
	format='%(asctime)s : %(levelname)s : %(message)s',
	level=logging.INFO)
corpus_path = 'corpus/'
cores = mp.cpu_count()
name_corpus = ['attraction_tag.list',
               'hotel_tag.list',
               'restaurant_tag.list']

name_model = ['model/attraction_tag.model',
              'model/hotel_tag.model',
              'model/restaurant_tag.model']

params_tag = [{'size':300, 'window':99999, 'min_count':0,        # Attraction
               'workers':cores, 'iter':100, 'sg':1, 'sample':1e-2},
              {'size':300, 'window':99999, 'min_count':0,        # Hotel
               'workers':cores, 'iter':100, 'sg':1, 'sample':1e-4},
              {'size':300, 'window':99999, 'min_count':0,        # Restaurant
               'workers':cores, 'iter':100, 'sg':1, 'sample':1e-4}]