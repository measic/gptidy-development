# plot solutions
plt.plot(linspace(2012,2013,1000), sol_n_lincs[:,1]+sol_n_lincs[:,2], label='N. Lincs')
plt.plot(linspace(2012,2013,1000), sol_haringey[:,1]+sol_haringey[:,2], label = 'Haringey')
plt.plot(linspace(2012,2013,1000), sol_dudley[:,1]+sol_dudley[:,2], label = 'Dudley')
plt.ylim(0,0.05)
plt.xlim(2012,2013)
plt.ylabel('Prevalence')
plt.xticks([2012,2013], ['2012','2013'])
plt.legend()