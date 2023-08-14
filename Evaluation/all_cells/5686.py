X_test = []
for s in test_sents:
    X_test.extend(sent2features(s))
    
y_test = []
for s in test_sents:
    y_test.extend(sent2labels(s))