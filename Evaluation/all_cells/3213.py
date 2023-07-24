#Run this cell multiple times to iterate through perceptron algorithm.
w = update_nueron(w, X[i, :], y[i])

#plot decision boundary and examples
plot_decision_boundary(X, y, w, i)

#Increment counter, startover when we reach the end of examples
i = (i+1)%X.shape[0] 