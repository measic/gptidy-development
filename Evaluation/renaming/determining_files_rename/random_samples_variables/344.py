PROJECT_DIR = '../../'
use_toy_data = False
LOG_DIR = 'logs'
if use_toy_data:
    batch_size = 8
    embedding_dim = 5
    cell_size = 32
    variable_def = 6
else:
    batch_size = 64
    embedding_dim = 20
    cell_size = 128
    variable_def = 33
use_attention = True
use_bidirectional_encoder = True
is_time_major = True