#row 1 subplot
plt.subplot(nrows, ncols, idx)
plt.plot(data,'b*')
plt.title('Raw data')
plt.xlim((-1,10))

#row 2 subplot
plt.subplot(nrows, ncols, idx+1)
err = np.std(data, axis=1)
plt.bar(x, fit_fn(x), color='r')
plt.errorbar(x, fit_fn(x), err, fmt='*g')
plt.xlim((-1,10))  #must set limits for each subplot or else it uses defaults.

plt.show()
plt.close()