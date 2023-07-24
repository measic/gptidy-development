al = deepcopy(abslookup_lm)
#al.absorptioncrosssection[al.absorptioncrosssection < 0] = np.nan
#a = abslookup_lm.absorptioncrosssection < 0
plt.pcolormesh(abslookup_lm.frequencygrid, abslookup_lm.pressuregrid,
               (al.absorptioncrosssection[0,4].T < 0).astype('int'))
               #np.log10(np.abs(al.absorptioncrosssection[0,4].T)))
plt.yscale('log')
#plt.xlim([17e12, 18e12])
plt.colorbar()