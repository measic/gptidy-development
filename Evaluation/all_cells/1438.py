plt.plot(data, 'bo')
x = np.arange(data.shape[0])
avg = np.average(data, axis=1)
fit = np.polyfit(x, avg, 1)
fit_fn = np.poly1d(fit)
plt.plot(x, fit_fn(x), 'r-^')
err = np.std(data, axis=1)
plt.errorbar(x, fit_fn(x), yerr=err, fmt='g-')
plt.savefig('Figure-Lesson8.png')
plt.show()  
plt.close()