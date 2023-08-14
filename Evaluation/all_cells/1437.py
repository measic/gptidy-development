err = np.std(data, axis=1)
print(err)
plt.errorbar(x, fit_fn(x), yerr=err, fmt='g-')