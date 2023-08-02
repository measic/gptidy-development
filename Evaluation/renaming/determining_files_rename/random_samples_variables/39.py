variable_def = B12_a[:, -1::-1]
HoM = hit_or_miss(X, variable_def)
plt.figure(figsize=[10, 10])
plt.subplot(1, 2, 1)
plt.imshow(X, interpolation='nearest')
plt.subplot(1, 2, 2)
plt.imshow(X, interpolation='nearest', alpha=0.8)
plt.imshow(HoM, interpolation='nearest', alpha=0.5)