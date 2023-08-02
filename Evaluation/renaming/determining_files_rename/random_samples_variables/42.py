result_test = []
result_train = []
tot = 0
for string in ['share', 'comment', 'zan', 'content_len', '链接', '//@', '@', '#', '【', '《', '\\[']:
    temp = []
    for i in test[string + '_histogram']:
        if isinstance(i, int):
            temp.append(np.zeros(shape=8))
            tot += 1
        else:
            temp.append(i[0])
    result_test.append(np.asarray(temp))
    temp = []
    for i in train[string + '_histogram']:
        temp.append(i[0])
    result_train.append(np.asarray(temp))
    train.drop(string + '_histogram', axis=1, inplace=True)
    test.drop(string + '_histogram', axis=1, inplace=True)
train.drop(['pid', 'uid'], inplace=True, axis=1)
test.drop(['pid', 'uid'], inplace=True, axis=1)
train_y = train[['share', 'comment', 'zan']].values
train.drop(['share', 'comme·nt', 'zan'], axis=1, inplace=True)
variable_def = train.values
test_x = test.values
for i in result_train:
    variable_def = np.c_[variable_def, i]
for i in result_test:
    test_x = np.c_[test_x, i]
np.save('processed_data/train3_np', variable_def)
np.save('processed_data/test3_np', test_x)
np.save('processed_data/target3_np', train_y)