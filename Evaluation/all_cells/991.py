scores = cross_val_score(logreg, X_copy,y, cv=10, scoring='accuracy')
print(scores.mean())