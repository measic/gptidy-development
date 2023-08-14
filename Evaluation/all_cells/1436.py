#obtain the fit parameters from linear regression
# x will be the row indices
x = range(data.shape[0])
print(x)
# for each row, find average across columns to make a 1D vector.
avg = np.average(data, axis=1)
print(avg)
fit = np.polyfit(x, avg, 1)
#obtain the function that represents the fit and can generate new values.
fit_fn = np.poly1d(fit)
#plot fit as red line with triangles.
plt.plot(x, fit_fn(x), 'r-^')
