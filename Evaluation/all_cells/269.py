# some simple testing code and such
dataset = 'mnist'
train_data = data_filepath+dataset+'_data_train.csv'
train_labels = data_filepath+dataset+'_labels_train.csv'
train_ids = data_filepath+dataset+'_ids_train.csv'
test_data = data_filepath+dataset+'_data_test.csv'
test_ids = data_filepath+dataset+'_ids_test.csv'
description = data_filepath+dataset+'_feature_descriptions.csv'

proc = Preprocessor(train_data_file=train_data,
                 train_label_file=train_labels,
                 train_ids_file=train_ids,
                 test_data_file=test_data,
                 test_ids_file=test_ids,
                 instr_file=description)

proc.read_data()

proc.process()

# doesn't do anything yet, hasn't been implemented
proc.select_features()

# data is written to output directory
# any existing data is overwritten
proc.write_data()
