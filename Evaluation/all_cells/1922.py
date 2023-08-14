plt.loglog(np.array(capacities), np.array(bloom_times_deletion), "-ro", ms=7, label="Counting bloom filter")
plt.loglog(np.array(capacities), np.array(cuckoo_times_deletion), "-go", ms=7, label="Cuckoo filter")
plt.xlim([10e1, 10e7])
plt.ylim([10e-4, 10e2])
plt.ylabel("Time (seconds)")
plt.xlabel("Number of items Deleted")
plt.title("Deletion Time")
plt.legend()
plt.savefig('images/deletion_time.pdf', bbox_inches='tight')