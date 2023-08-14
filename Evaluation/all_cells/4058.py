# plot solutions
plt.plot(linspace(2012,2013,1000), sol_12_13[:,1]+sol_12_13[:,2], label='2012-2013')
plt.plot(linspace(2013,2014,1000), sol_13_14[:,1]+sol_13_14[:,2], label='2013-2014')
plt.plot(linspace(2014,2015,1000), sol_14_15[:,1]+sol_14_15[:,2], label='2014-2015')
plt.ylim(0,0.025)
plt.ylabel('Prevalence')
plt.xticks([2012,2013,2014,2015], ['2012','2013','2014','2015'])
plt.legend(loc=4)