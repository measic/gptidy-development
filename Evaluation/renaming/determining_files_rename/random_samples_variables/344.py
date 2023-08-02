PROJECT_DIR = '../../'
use_toy_data = False
LOG_DIR = 'logs'
if use_toy_data:
    batch_size = 8
    embedding_dim = 5
    variable_def = 32
    max_len = 6
else:
    batch_size = 64
    embedding_dim = 20
    variable_def = 128
    max_len = 33
use_attention = True
use_bidirectional_encoder = True
is_time_major = True