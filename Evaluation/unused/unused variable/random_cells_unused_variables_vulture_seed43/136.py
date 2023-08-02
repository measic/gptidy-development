train_uid = access_data.load_processed_data('uid&pid_train')
test_uid  = access_data.load_processed_data('uid&pid_test')

train ,test = access_data.load_raw_data()

train_corpus = access_data.load_processed_data('cleaned&segment_train')
test_corpus  = access_data.load_processed_data('cleaned&segment_test')                                               
train = pd.concat([train_uid,train,train_corpus],axis=1)
test  = pd.concat([test_uid,test,test_corpus],axis=1)

train.drop([0,1],axis=1,inplace=True)
test.drop([0,1],axis=1,inplace=True)

train.columns = ['pid','uid','time','share','comment','zan','raw_corpus','clean&segment','链接','//@','@','#','【','《','\[']
test.columns = ['pid','uid','time','raw_corpus','clean&segment','链接','//@','@','#','【','《','\[']
train['uid'] = train['uid'].astype(np.uint16)
test['uid']  = test['uid'].astype(np.uint16)
l = ['链接','//@','@','#','【','《','\[']

for string in l :
    train[string] = train[string].astype(np.int8)
    test[string]  = test[string].astype(np.int8)

#在training set和test set中和用户发送微博的总数量
tot = pd.concat([pd.DataFrame(train['uid']),pd.DataFrame(test['uid'])])
c = pd.DataFrame(tot['uid'].value_counts())
c.columns = ['tot_counts']
train = train.merge(c,left_on='uid',right_index=True,how='left')
test  = test.merge(c,left_on='uid',right_index=True,how='left')

# 用户出现在训练集的次数
c = pd.DataFrame(train['uid'].value_counts())
c.columns = ['train_counts']
train = train.merge(c,left_on='uid',right_index=True,how='left')
test  = test.merge(c,left_on='uid',right_index=True,how='left')

test.fillna(-1,inplace=True)
train['tot_counts'] = train['tot_counts'].astype(np.int32)
train['train_counts'] = train['train_counts'].astype(np.int32)

test['tot_counts'] = test['tot_counts'].astype(np.int32)
test['train_counts'] = test['train_counts'].astype(np.int32)

addr1 = setting.raw_data_dir + 'basic_train'
addr2 = setting.raw_data_dir + 'basic_test'

lda_result = np.load('processed_data/lda_result_version3.npy')
lda_result = pd.DataFrame(lda_result,columns=['topic_%d' %i for i in range(0,25)])

for string in ['topic_%d' %i for i in range(0,25)]:
    train[string] = lda_result.loc[:train.shape[0]-1,string].values
    test[string] = lda_result.loc[train.shape[0]:,string].values

#train.to_pickle(addr1)
#test.to_pickle(addr2)