xbar = np.mean(counts, axis=1)
s = np.std(counts, axis=1)

#fit polynomial
x_arr = np.arange(0, 10**5, 10**2)
fit = np.polyfit(xbar, s**2, 2)
y_arr = np.polyval(fit, x_arr)

#plot data
plt.scatter(xbar, s**2, marker='x', s=50, color='k', label='Data')
#plot 2nd degree polynomial
coeff = [np.round(f,1-int(math.floor(math.log10(abs(f))))) for f in fit]
plt.plot(x_arr, y_arr, label=r'$f(x)=%s x^2 + %s x + %s$'%(coeff[0], coeff[1], coeff[2]))

plt.xlim(100, 5*10**4)
plt.ylim(50, 10**5)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Mean (ADU)')
plt.ylabel('Variance (ADU$^2$)')
plt.legend(loc='upper left', scatterpoints=1)
plt.savefig('writeup/plots/mean_vs_variance.png')
plt.show()