# tej colonnes où y'a des -999

x[x==-999]=np.NaN
z=x[:,~np.isnan(x).any(axis=0)] #z is our matrix of observations with size (number of observations, number of features without -999)

#z=one_hot_jet_num(z,17)
#z=build_poly_with_one_hot(z,5,17,True,3)

#z2=interaction_prod(z,0,False)
#z1 = build_poly(z,3)
#z3=build_poly(z2,3)
#z = np.c_[z1,z2]
#z=np.c_[z1,z3]
#add_ones(z)
#np.column_stack((z, np.ones(z.shape[0])))
#np.column_stack((z, np.ones(z.shape[0])))
print(z.shape)