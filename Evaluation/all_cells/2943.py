#train_basic = pd.read_pickle('raw_data/basic_train')
#test_basic  = pd.read_pickle('raw_data/basic_test')
#train_basic = train_basic.loc[1626750:]
#计算情感极性
begin_time= time.time()
train_sentiment,test_sentiment = feature.sentiment_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#计算一周内出现微博的数量
begin_time= time.time()
train_seven_days ,test_seven_days = feature.find_seven_days(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#lda特征
begin_time = time.time()
train_lda_feature,test_lda_feature = feature.lda_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#用户特征
begin_time= time.time()
train_user,test_user = feature.user_basic_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#文本特征
begin_time= time.time()
train_content,test_content = feature.content_basic_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#时间特征
begin_time= time.time()
train_time,test_time = feature.time_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time
#关键词特征
begin_time = time.time()
train_keyword,test_keyword = feature.key_word_feature(train_basic,test_basic)
end_time = time.time()
print end_time - begin_time