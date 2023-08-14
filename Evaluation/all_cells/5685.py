%%time

X_train = []
for s in train_sents:
    X_train.extend(sent2features(s))
    
y_train = []
for s in train_sents:
    y_train.extend(sent2labels(s))
