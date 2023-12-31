#result from running this once. takes more than 10mins, so not running multiple times. 
plt.loglog(np.array(capacities), np.array(bloom_times), "-ro", ms=7, label="Counting Bloom filter")
plt.loglog(np.array(capacities), np.array(cuckoo_times), "-go", ms=7, label="Cuckoo Filter")
plt.xlim([10e1, 10e7])
plt.ylim([5.0 * 10e-6, 10e4])
plt.ylabel("Time (seconds)")
plt.xlabel("Number of items inserted")
plt.title("Insertion Time")
plt.legend()
plt.savefig('images/insertion_time.pdf', bbox_inches='tight')