train_corpus ,test_corpus = preprocessing.clean_corpus()
test_corpus['corpus'] = preprocessing.segment_word(test_corpus['corpus'])
train_corpus['corpus'] = preprocessing.segment_word(train_corpus['corpus'])

train_corpus.to_pickle(setting.processed_data_dir+'cleaned&segment_train')
test_corpus.to_pickle(setting.processed_data_dir+'cleaned&segment_test')

train_uid,test_uid = preprocessing.encode_label()

preprocessing.bag_of_word(train_corpus['corpus'].values,test_corpus['corpus'].values,min_df=10)