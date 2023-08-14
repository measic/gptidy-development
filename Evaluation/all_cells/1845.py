#Importing this because of deprecation warnings cluttering the output
import warnings
warnings.filterwarnings('ignore')

# Start the bottom up feature selection
# Compute the accuracy of logistic regression with N features

train = X_train
dev = X_dev

bestVec = [] 

for j in range(15):
    maxacc = 0
    maxi = 0
    for i in range(15):
        if i not in bestVec:
            X_train_eng = pd.DataFrame(train.ix[:, bestVec + [i]])
            X_dev_eng = pd.DataFrame(dev.ix[:, bestVec + [i]])
            m=0.5
            lrq = LogisticRegression(C = m, penalty = 'l2')
            lrq.fit(X_train_eng, y_train)
            if lrq.score(X_dev_eng, y_dev) > maxacc:
                maxacc = lrq.score(X_dev_eng, y_dev)
                maxi = i
    bestVec = bestVec + [maxi]
    print 'At number of features =', j+1,'the best feature to add is', predictors[maxi],'and the accuracy is %.10f' % maxacc