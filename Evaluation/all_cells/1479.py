#revise the above graph to use a different line width,color and no symbols
plt.subplot(nrows, ncols, idx)
plt.plot(x1, y1, '-', color='cyan') #changes
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(nrows, ncols, idx+1)
plt.plot(x2, y2, '--', linewidth=4) #changes
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.show()
plt.close() #do this at end of each plot