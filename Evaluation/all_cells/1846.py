#Tested for C in 0.00001, 0.0001, 0.001, 0.01, 0.1,, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0
#Highest accuracy is when C=0.5

for m in [0.5]: # 0.00001, 0.0001, 0.001, 0.01, 0.1,, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0
    lrq = LogisticRegression(C = m, penalty = 'l2')
    lrq.fit(X_train, y_train)
    weight1 = lrq.coef_
    sum1 = sum(sum(weight1))
    print 'Accuracy at C=0.5:', lrq.score(X_dev, y_dev)
    print 'Sum of Squared Weight:', sum1
