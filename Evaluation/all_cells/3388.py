
y = diva.to_encoding(gt)
# y[np.where(y[:,:,3] == 0)].shape
plt.imshow(y[:,:,3] < 1, 'binary')