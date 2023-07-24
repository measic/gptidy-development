#arrangement of subplots
nrows = 2
ncols = 1
idx = 1
#row 1 subplot
plt.subplot(nrows, ncols, idx)
plt.plot(data,'b*')
plt.title('Raw data')

#row 2 subplot
plt.subplot(nrows, ncols, idx+1)
plt.bar(x, fit_fn(x), color='r')
plt.show()
plt.close()