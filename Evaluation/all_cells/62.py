import numpy as np
X = np.zeros((100, 150), dtype=bool)
X[30, :] = 1
X[:, 65] = 1
X[35:45, 35:50] = 1
X[40:50,100:110] = 1
X[52:82,100:110] = 1
X[50:52,105:106] = 1
X[45:46,105:106] = 0
X[70:72,104:106] = 0
X[64:67,103:106] = 0

B = square(3)
X_dil = dilation(X,selem=B)
X_ero = erosion(X,selem=B)

X_open = dilation(X_ero,selem=B)
X_close = erosion(X_dil,selem=B)

plt.figure(figsize=[10,10])
plt.subplot(3,2,1)
plt.imshow(X,interpolation='nearest',cmap=plt.cm.gray)
plt.title('$X$')
plt.subplot(3,2,3)
plt.imshow(X_ero,interpolation='nearest',cmap=plt.cm.gray)
plt.title('erosion of $X$ by $B$')
plt.subplot(3,2,4)
plt.imshow(X_dil,interpolation='nearest',cmap=plt.cm.gray)
plt.title('dilation of $X$ by $B$')
plt.subplot(3,2,5)
plt.imshow(X_open,interpolation='nearest',cmap=plt.cm.gray)
plt.title('opening of $X$ by $B$')
plt.subplot(3,2,6)
plt.imshow(X_close,interpolation='nearest',cmap=plt.cm.gray)
plt.title('closing of $X$ by $B$');
