from skimage.morphology import disk,erosion,dilation,square
B = square(3)
X_dil = dilation(X,selem=B)
X_ero = erosion(X,selem=B)

plt.figure(figsize=[10,5])
plt.subplot(1,3,1)
plt.imshow(X,interpolation='nearest',cmap=plt.cm.gray)
plt.title('$X$')
plt.subplot(1,3,2)
plt.imshow(X_dil,interpolation='nearest',cmap=plt.cm.gray)
plt.title('dilation of $X$ by $B$')
plt.subplot(1,3,3)
plt.imshow(X_ero,interpolation='nearest',cmap=plt.cm.gray)
plt.title('erosion of $X$ by $B$')
plt.figure(figsize=[6,6])
plt.imshow(X,interpolation='nearest',cmap=plt.cm.gray,alpha=.3)
plt.imshow(X_ero,interpolation='nearest',cmap=plt.cm.gray,alpha=.3)
plt.imshow(X_dil,interpolation='nearest',cmap=plt.cm.gray,alpha=.3);