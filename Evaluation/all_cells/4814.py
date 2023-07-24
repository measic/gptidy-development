names = {'student_1': "Lucas Zweili",
        'student_2': "Raphaël Reis Nunes"}

sciper = {'student_1': 264542, 
          'student_2': 256364}

seed = sciper['student_1']+sciper['student_2']

%matplotlib inline

#GPU acceleration
from tensorflow.python.client import device_lib
from keras import backend as K
K.tensorflow_backend._get_available_gpus()
print(device_lib.list_local_devices())

import numpy as np
import matplotlib.pyplot as plt
import os, sys
import copy

plt.rcParams['font.size'] = 28
plt.style.use('ggplot')
plt.rcParams["axes.grid"] = False
c = plt.rcParams['axes.prop_cycle'].by_key()['color']

import keras
from keras.models import Model, load_model
from keras.layers import Input, Masking, Reshape, TimeDistributed, Dense, Flatten, Concatenate, Dropout, LSTM, CuDNNLSTM, GRU, CuDNNGRU, SimpleRNN, Bidirectional, Embedding, BatchNormalization
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import ModelCheckpoint, EarlyStopping


def getRawDataFromFile(datapath="../../personachat/", file="train_both_revised.txt"):
    
    f = open(datapath+file)

    conversations = []
    current_conversation = []
    
    for l, line in enumerate(f):
        #print(l, line)
        if "persona:" in line:
            if len(current_conversation) > 1:
                conversations.append(current_conversation)
            current_conversation = [] 
            continue

        #remove numberings
        processed_line = line.split(' ')
        processed_line = " ".join(processed_line[1:])
        line = processed_line
        #print(line)

        conv = line.split('\t')    
        q = conv[0]
        a = conv[1]
        current_conversation.append(q)
        current_conversation.append(a)
    
    return conversations 