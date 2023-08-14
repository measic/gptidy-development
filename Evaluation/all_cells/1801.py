x = np.arange(0,40,1)
for mu in range(1,30,3): 
    pdist1 = poisson.pmf(x, mu)
    pdist1 = pdist1/max(pdist1)
    pdist2 = poisson_approx(x, mu)
    
    if mu == 1:
        plt.plot(x, pdist1, linewidth=.5, label='scipy')
        plt.plot(x, pdist2, linestyle='dashed', label='Sterling factorial')
    else:
        plt.plot(x, pdist1, linewidth=.5)
        plt.plot(x, pdist2, linestyle='dashed')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel(r'$P(x;\mu)$')
plt.savefig('writeup/plots/poisson_comparisons.png')
plt.show()