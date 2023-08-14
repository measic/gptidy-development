from sklearn.linear_model import LogisticRegression

trainere = LogisticRegression(multi_class='multinomial',solver='newton-cg')
trainere.fit(finalX,y_train)
