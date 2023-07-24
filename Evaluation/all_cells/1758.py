# Do EVD to see the projection matrix
cov        = X.T @ X /(X.shape[0] - 1)
val,vec    = np.linalg.eigh(cov)
idx        = np.argsort(val)[::-1]; val = val[idx]; vec = vec[:,idx]
project_X  = X   @ vec;                      project_V  = vec.T @ vec
revert_X   = project_X @ np.linalg.inv(vec) ;revertedV  = project_V @ np.linalg.inv(vec).T

plt.figure(figsize=(15,5)); 

plt.subplot(131); 
plt.scatter(X[y==0, 0], X[y==0, 1], color='red',  alpha=0.5)
plt.scatter(X[y==1, 0], X[y==1, 1], color='blue', alpha=0.5)
pca11=plt.arrow   (0, 0, *vec[:,0] * val[0], head_width=0.05, head_length=0.05,color='Green',  label='First PC')
pca12=plt.arrow   (0, 0, *vec[:,1] * val[1], head_width=0.05, head_length=0.05,color='magenta',label='Second PC')
plt.grid(True); 

plt.subplot(132); 
plt.scatter(project_X[y==0, 0], project_X[y==0, 1], color='red',  alpha=0.5)
plt.scatter(project_X[y==1, 0], project_X[y==1, 1], color='blue', alpha=0.5)
pca21=plt.arrow   (0, 0, *project_V[:,0] * val[0], head_width=0.05, head_length=0.05,color='Green',  label='First PC')
pca22=plt.arrow   (0, 0, *project_V[:,1] * val[1], head_width=0.05, head_length=0.05,color='magenta',label='Second PC')
plt.grid(True); 

plt.subplot(133); 
plt.scatter(revert_X[y==0, 0], revert_X[y==0, 1], color='red',  alpha=0.5)
plt.scatter(revert_X[y==1, 0], revert_X[y==1, 1], color='blue', alpha=0.5)
pca21=plt.arrow   (0, 0, *revertedV[:,0] * val[0], head_width=0.05, head_length=0.05,color='Green',  label='First PC')
pca22=plt.arrow   (0, 0, *revertedV[:,1] * val[1], head_width=0.05, head_length=0.05,color='magenta',label='Second PC')
plt.grid(True); 

plt.show()