res = {}
for (name, prd) in ('lr', log_clf), ('rf', rnd_clf), ('svc', svm_clf):
    predictions = prd.predict(X_test)
    res[name] = predictions

correct = 0
wrong = 0
for i in range(len(y_test)):
    outcome = (res['lr'][i] + res['rf'][i] + res['svc'][i]) > 1
    if avgprob[0] < avgprob[1]: 
        outcome = 1
    if outcome == y_test[i]: correct += 1
    else: wrong += 1
print(correct/(correct + wrong))