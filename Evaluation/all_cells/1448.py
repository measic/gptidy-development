#Here is the pythonic (faster) alternative.
mdat = np.array([np.mean(data[cat==i+1]) for i in range(0,3)])
print(mdat)
