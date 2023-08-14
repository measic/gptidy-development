# perfroming  linear regression with scikit package
errors =[]
kFolds =10
for s in getListOfFiles('Data/'):
        data = getListFromAFile("Data/"+s)
        kf = sklearn.cross_validation.KFold(n=len(data[0]), n_folds=kFolds, shuffle=False,random_state=None)
        error = 0
        regression = linear_model.LinearRegression()
        for train_index, test_index in kf:
#           print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test =data[0][train_index], data[0][test_index]
            y_train, y_test = data[1][train_index], data[1][test_index]
            regression.fit(X_train.reshape(-1, 1),y_train)
            error = error + mean_squared_error(y_test,regression.predict(X_test.reshape(-1, 1)))
       
        error = error/kFolds
        createPlots( data[0].reshape(-1, 1),data[1],xlabel="x-axis -->",ylabel="y-axis -->",title="s:"+s+"|degree:linear reegression",plotterRef=regression.predict)
        errors.append({'file':s,'mse':error})
    

print errors
df = pd.DataFrame(errors)
print df