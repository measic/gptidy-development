#counts per second
xbar_cps = np.mean(counts_ps, axis=1)
s_cps = np.std(counts_ps, axis=1)

#number of frames per exposure
num_per_dir = [len(os.listdir('data/'+f)) for f in files]
nframes = [sum(num_per_dir[0:i]) for i in range(len(files))]

plt.plot(nframes, xbar_cps, marker='x', color='k')
plt.plot(nframes, s_cps, marker='x', color='b')
plt.xlabel('Number of Frames')
plt.ylabel('MOM (ADU/s)')
plt.savefig('writeup/plots/exptime_vs_meancount.png')
plt.show()


#



