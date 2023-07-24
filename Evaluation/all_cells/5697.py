import sys
from collections import defaultdict
import math
import logging

#import emission_counts
#import transition_counts

"""
Usage:
python viterbi.py ner.counts ngram.counts ner_dev.dat > [output_file]
Implementation of the Viterbi algorithm
Calculate emission e(x|y) and trigram probability based on data 
in ner_counts,
Read ner_dev.dat, output prediction to [output_file]
"""


# Go through dev data, predict tag & compute probability based on model abov
log_probability = 0
y_predict = []
y_actual = []
# First round for q(*, *, y_1)
first_round = True
for sent in test_sents:
    log_probability = 0
    first_round = True
    for i in  range(len(sent)):
        word = sent[i][0]
        # Check if there is an existing label associated to the word
        if word in counter.count_xy:
            max_probability = 0
            for label in list(counter.count_xy[word]):
                # Calculate e(x|y)
                emission = float(counter.count_xy[word][label]) / float(counter.count_y[label])
                # Calculate q(y| y_i-2, y_i-1)
                # Check for first round
                if first_round:
                    y_2 = '*'
                    y_1 = '*' 
                    first_round = False
                bigram = y_2 + ' ' + y_1
                trigram = y_2 + ' ' + y_1 + ' ' + label
                parameter = 0.0000000001
                if trigram in counter.trigram_counts:
                    parameter = float(counter.trigram_counts[trigram])/float(counter.bigram_counts[bigram])
                probability = parameter*emission
                if probability > max_probability:
                    max_probability = probability
                    arg_max = label	
        
            log_probability = log_probability + math.log(max_probability)
            y_actual.append(sent[i][2])
            y_predict.append(arg_max)
            y_2 = y_1
            y_1 = arg_max
        else:
            y_predict.append('O')
            y_actual.append(sent[i][2])
            

#     # If Count(x~>y) = 0, use _RARE_ 
#     else:
#         for label in list(count_xy['_RARE_']):
#             # Calculate e(_RARE_|y)
#             probability = 0
#             emission = float(count_xy['_RARE_'][label]) / float(count_y[label])
#             # Calculate q(y| y_i-2, y_i-1)
#             # Check for first round
#             if first_round:
#                 y_2 = '*'
#                 y_1 = '*' 
#                 first_round = False
#             bigram = y_2 + ' ' + y_1
#             trigram = y_2 + ' ' + y_1 + ' ' + label
#             parameter = 0.0000000001
#             if trigram in trigram_counts:
#                 parameter = float(trigram_counts[trigram])/float(bigram_counts[bigram])
#             probability = parameter*emission
#             if probability > max_probability:
#                 max_probability = probability
#                 arg_max = label