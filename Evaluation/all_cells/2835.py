# How many features were eliminated? 
print("Lasso picked " + str(sum(coef_lasso != 0)) + " features and eliminated the other " + str(sum(coef_lasso == 0)) + " features")