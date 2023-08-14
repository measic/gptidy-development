train_basic.drop(['uid','pid','time','share','comment','zan','raw_corpus','clean&segment'],axis=1,inplace=True)
test_basic.drop(['uid','pid','time','raw_corpus','clean&segment'],axis=1,inplace=True)
train_user = pd.concat([train_user,train_basic],axis=1)
test_user  = pd.concat([test_user,test_basic],axis=1)

train = train_user.merge(train_content,how='left',left_on='pid',right_index=True)
test  = test_user.merge(test_content,how='left',left_on='pid',right_index=True)

train = train.merge(train_time,how='left',left_on='pid',right_index=True)
test  = test.merge(test_time,how='left',left_on='pid',right_index=True)

train = pd.concat([train,train_keyword],axis=1)
test  = pd.concat([test,test_keyword],axis=1)

train = train.merge(train_lda_feature,how='left',left_on='pid',right_index=True)
test  = test.merge(test_lda_feature,how='left',left_on='pid',right_index=True)

train = train.merge(train_sentiment,how='left',left_on='pid',right_index=True)
test  = test.merge(test_sentiment,how='left',left_on='pid',right_index=True)

train = train.merge(train_seven_days,how='left',left_on='pid',right_index=True)
test  = test.merge(test_seven_days,how='left',left_on='pid',right_index=True)

begin_time = time.time()
result,gmm = feature.clustering_feature(train,test)
end_time = time.time()
print end_time - begin_time

train = train.merge(result,how='left',left_on='uid',right_index=True)
test  = test.merge(result,how='left',left_on='uid',right_index=True)