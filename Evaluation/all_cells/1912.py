plt.loglog(np.array(capacities), np.array(bloom_fp), "-ro", ms=7, label="Counting Bloom filter")
plt.loglog(np.array(capacities), np.array(cuckoo_fp), "-go", ms=7, label="Cuckoo Filter")
plt.axhline(y=0.03, xmin=0, xmax=1, hold=None, ls="--")
plt.xlim([2.5*10e1, 10e7])
plt.ylim([10e-65, 10e10])
plt.ylabel("False Positive Rate")
plt.xlabel("Capacity (Max # items inserted)")
plt.legend()
plt.savefig('images/false_positive_test.png', bbox_inches='tight')