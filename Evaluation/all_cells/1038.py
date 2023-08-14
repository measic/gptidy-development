lmin=-10
lmax=0
n=10
y=Strain1_y
x=Strain1_z
y_te=Stest1_y
x_te=Stest1_z
ratio=[]
ratios=[]
weights=[]
lambdas = np.logspace(lmin, lmax, n)
for ind, lambda_ in enumerate(lambdas):
    weight = ridge_regression(y, x, lambda_)
    ratio.append(ratio_prediction_threshold(y_te,x_te,weight,-0.1))
    ratios.append(ratio_prediction_threshold(y_te,x_te,weight,0.1))
    weights.append(weight)
    print(ind)
indx1=np.argmax(ratio)
indx2=np.argmax(ratios)
weight=weights[indx]
lambdaa=lambdas[indx]
