PAD = 0                            # Value for PADding images
POS = 1                            # Values of positive and negative label 0/-1
NEG = 0

POS_SPAN = 1                             # Number of positive values around true position (5 is too high)
POS_WEIGHT = 3                           # Weighting possitive values in loss counting

slider_size = (60, 60)                   # Height is set to 60 by data and width should be even
N_INPUT = slider_size[0]*slider_size[1]  # Size of sequence input vector will depend on CNN
num_buckets = 5
n_classes = 2                            # Number of different outputs

rnn_layers = 4
rnn_residual_layers = 2                  # HAVE TO be smaller than encoder_layers
rnn_units = 256

learning_rate = 1e-4
dropout = 0.4                            # Percentage of dopped out data
train_set = 0.8                          # Percentage of training data

TRAIN_STEPS = 500000                     # Number of training steps!
TEST_ITER = 150
LOSS_ITER = 50
SAVE_ITER = 2000
BATCH_SIZE = 10
# EPOCH = 2000                           # "Number" of batches in epoch

save_loc = 'models/gap-clas/RNN/Bi-RNN-dense'