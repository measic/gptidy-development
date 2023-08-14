x_test[x_test==-999]=np.NaN
z_test=x_test[:,~np.isnan(x_test).any(axis=0)] #z is our matrix of observations with size (number of observations, number of features without -999)
z1_test = build_poly(z_test,9)
z2_test=interaction_prodbis(z_test,0,False)
z3_test=build_poly(z2_test,6)
z_test = np.c_[z1_test,z3_test]
#z_test=np.c_[z1_test,z3_test]