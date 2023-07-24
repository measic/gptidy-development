corpus    = "BrentProvidence"
providence_data_file = os.path.join("data/words_sentences/providence_avg_prosody_pos.csv")
brent_data_file      = os.path.join("data/words_sentences/brent_avg_prosody_pos.csv")
both_data_file       = os.path.join("data/words_sentences/brentprovidence_avg_prosody_pos.csv")

# define x-fields (column IDs) to keep at 1    = word itself
#                                         2    = pos
#                                         3    = length (letters)
#                                         4    = frequency
#                                         5-93 = egemaps prosody features
features  = list(range(1,93))

pos_filter = None  #[['pos', 'nouns','function_words']]

# define name (col header) of y-variable in data file
y         = 'y'

# load data, x-fields, y-field, train/dev/test split from input file
print("extracting providence...")
providence_x_train, providence_y_train, _, _, _, _, labels = get_data_from_tsv(providence_data_file, 
                                                                      x_fields=features, 
                                                                      y_field=y, 
                                                                      x_filter=pos_filter,
                                                                      train_portion=1.0,
                                                                      shuffle=False)
print("extracting brent...")
brent_x_train, brent_y_train, _, _, _, _, labels = get_data_from_tsv(brent_data_file, 
                                                                      x_fields=features, 
                                                                      y_field=y, 
                                                                      x_filter=pos_filter,
                                                                      train_portion=1.0,
                                                                      shuffle=False)

print("extracting brentprovidence...")
both_x_train, both_y_train, _, _, _, _, labels = get_data_from_tsv(both_data_file, 
                                                                      x_fields=features, 
                                                                      y_field=y, 
                                                                      x_filter=pos_filter,
                                                                      train_portion=1.0,
                                                                      shuffle=False)

if corpus == "Providence":
    x_train = providence_x_train
    y_train = providence_y_train
elif corpus == "Brent":
    x_train = brent_x_train
    y_train = brent_y_train
elif corpus == "BrentProvidence":
    x_train = both_x_train
    y_train = both_y_train

first_numeric_feature = x_train.columns.tolist().index('log_length')
first_egemaps_feature = x_train.columns.tolist().index('F0semitoneFrom27.5Hz_sma3nz_amean')

print(first_numeric_feature,first_egemaps_feature)