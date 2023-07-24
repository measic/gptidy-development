plt.fill_between(load_factors_emp, cuckoo_times_array[:,0], cuckoo_times_array[:,2], alpha=0.2)
plt.plot(load_factors_emp, cuckoo_times_array[:,1], "-go", label="Cuckoo Filter")

plt.fill_between(load_factors_emp, bloom_times_array[:,0], bloom_times_array[:,2], alpha=0.2)
plt.plot(load_factors_emp, bloom_times_array[:,1], "-ro", label="Counting Bloom Filter")


plt.ylabel("Time (seconds)")
plt.xlabel("Filter Occupancy")
plt.xlim([0, 1])
plt.legend()
plt.savefig('images/load_factor.png', bbox_inches='tight')