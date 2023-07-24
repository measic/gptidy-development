class CustomHyothesis:
    def createtor(self):
        aMatrixValueStore = [sum(map(lambda x: x**i, self.xlist)) for i in range(0, (self.degree*2) + 1)]
        bMatrixValueStore = [sum([(item*self.ylist[tv1]) for tv1, item in enumerate(map(lambda x: x**i, self.xlist))]) for i in range(0, self.degree + 1)]
        MatrixA = [aMatrixValueStore[i:(i+self.degree+1)] for i in range(0, self.degree + 1)]
        A = np.matrix(MatrixA)
        B = np.array(bMatrixValueStore)
        self.coeff = np.linalg.solve(A, B.T)
    
    def fit(self, degree, xlist, ylist):
        assert(degree > 0)
        assert(len(xlist) == len(ylist))
        
        self.degree = degree
        self.xlist = xlist
        self.ylist = ylist
        self.createtor()
    
    def predict(self, inList):
        return [sum([self.coeff[j]*(i**j) for j in range(0, self.degree + 1)]) for i in inList]

# predicting with kfols and checking oerror wof the custom class
errors = []
kFolds = 10
for itration in range(1, 7):
    for s in getListOfFiles('Data/'):
        data = getListFromAFile("Data/" + s)
        kf = sklearn.cross_validation.KFold(n=len(data[0]), n_folds=kFolds, shuffle=False, random_state=None)
        error = 0
        regression = CustomHyothesis()
        for train_index, test_index in kf:
            X_train, X_test = data[0][train_index], data[0][test_index]
            y_train, y_test = data[1][train_index], data[1][test_index]
            regression.fit(itration, X_train, y_train)
            error = error + mean_squared_error(y_test, regression.predict(X_test))
           
        error = error / kFolds
        errors.append({'degree': itration, 'file': s, 'mse': error})
        createPlots(data[0], data[1], "x-axis -->", "y-axis -->", title=str({'degree': itration, 'file': s}), plotterRef=regression.predict)    

df = pd.DataFrame(errors)
print(df)

for s in getListOfFiles('Data/'):
    data = getListFromAFile("Data/" + s)
    regression = CustomHyothesis()
    regression.fit(5, data[0], data[1])
    #plt.scatter(data[0], regression.predict(data[0]), alpha=0.5, color='r') 
    #plt.scatter(data[0], data[1], alpha=0.5, color='b')
    #plt.show()