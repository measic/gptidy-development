etime, temp = [], []
for exp in os.listdir('data/'):
    fdir = 'data/%s/'%(exp)
    for file in os.listdir(fdir):
        hdr = fits.open(fdir + file)
        data = np.array(hdr[0].data).flatten()
        etime.append(hdr[0].header['EXPTIME'])
        temp.append(hdr[0].header['TEMPDET'])
        
plt.scatter(etime, temp)
plt.xscale('log')
plt.xlabel('Exposure Time (sec)')
plt.ylabel('Detector Temperature (C)')
plt.xlim(10,1000)
plt.savefig('writeup/plots/exposure_temp.png')
plt.show()