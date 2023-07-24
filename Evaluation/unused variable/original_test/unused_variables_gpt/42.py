new_pc = eigvecs[:,-2:]

plt.figure(figsize=(15,5)); 

plt.subplot(121); 
plt.scatter(X[y==0, 0], X[y==0, 1], color='red',  alpha=0.5)
plt.scatter(X[y==1, 0], X[y==1, 1], color='blue', alpha=0.5)
plt.arrow   (0, 0, *vec[:,0] * val[0], head_width=0.05, head_length=0.05,color='Green',  label='First PC')
plt.arrow   (0, 0, *vec[:,1] * val[1], head_width=0.05, head_length=0.05,color='magenta',label='Second PC')
plt.grid(True); 

new_pc_cen = new_pc - new_pc.mean(0,keepdims=True)
cov        = new_pc_cen.T @ new_pc_cen /(new_pc_cen.shape[0] - 1)
val,vec    = np.linalg.eigh(cov)

plt.subplot(122); 
plt.scatter(new_pc[y==0, 0], new_pc[y==0, 1], color='red',  alpha=0.5)
plt.scatter(new_pc[y==1, 0], new_pc[y==1, 1], color='blue', alpha=0.5)
plt.arrow   (0, 0, *vec[:,0] * val[0], head_width=0.005, head_length=0.005,color='Green',  label='First PC')
plt.arrow   (0, 0, *vec[:,1] * val[1], head_width=0.005, head_length=0.005,color='magenta',label='Second PC')
plt.grid(True); 

plt.show()