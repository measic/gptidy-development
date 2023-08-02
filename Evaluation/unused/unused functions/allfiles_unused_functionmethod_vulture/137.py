CSV_COLUMNS = 'weight_pounds,is_male,mother_age,plurality,gestation_weeks,key'.split(',')
LABEL_COLUMN = 'weight_pounds'
KEY_COLUMN = 'key'
DEFAULTS = [[0.0], ['null'], [0.0], ['null'], [0.0], ['nokey']]
TRAIN_STEPS = 1000

def read_dataset(prefix, pattern, batch_size=512):
    # use prefix to create filename
    filename = 'gs://{}/babyweight/preproc/{}*{}*'.format(BUCKET, prefix, pattern)
    if prefix == 'train':
        mode = tf.estimator.ModeKeys.TRAIN
        num_epochs = None # indefinitely
    else:
        mode = tf.estimator.ModeKeys.EVAL
        num_epochs = 1 # end-of-input after this
    
    # the actual input function passed to TensorFlow
    def _input_fn():
        # could be a path to one file or a file pattern.
        input_file_names = tf.train.match_filenames_once(filename)
        filename_queue = tf.train.string_input_producer(
            input_file_names, shuffle=True, num_epochs=num_epochs)
 
        # read CSV
        reader = tf.TextLineReader()
        _, value = reader.read_up_to(filename_queue, num_records=batch_size)
        if mode == tf.estimator.ModeKeys.TRAIN:
          value = tf.train.shuffle_batch([value], batch_size, capacity=10*batch_size, 
                                         min_after_dequeue=batch_size, enqueue_many=True, 
                                         allow_smaller_final_batch=False)
        value_column = tf.expand_dims(value, -1)
        columns = tf.decode_csv(value_column, record_defaults=DEFAULTS)
        features = dict(zip(CSV_COLUMNS, columns))
        features.pop(KEY_COLUMN)
        label = features.pop(LABEL_COLUMN)
        return features, label
  
    return _input_fn