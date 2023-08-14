# Creating MOM and SDOM

# Pulls all the files together
# assums all the frames are in one directory
# Creates an array with all the file names
files = np.array(natsorted(os.listdir()))


data = []

# Go through each frame, take the median, subtract bias, and divide 
# by exposure time
for i in files:

    # loading in the data
    frame_data = fits.getdata(i)
    frame_exp = fits.open(i)
    exp_time = frame_exp[0].header['EXPTIME']
    # Subtracting the bias
    data_subbed = frame_data - bias_2D
    data_median_ps = np.median(data_subbed,axis=0)/exp_time
    # Median of each frame divided by exposure time for that frame
    data.append(data_median_ps)
   
data = np.array(data)

# Setting up arrays 
mom = []
std = []
num_frame = np.arange(2,len(data)+1)

# Calculates MOM and SDOM 
i = 2
while i < len(data)+1:
    frames = data[:i]
    mean = np.mean(frames) 
    stand = np.std(frames)
    mom.append(mean)
    std.append(stand)
    i = i + 1
    
mom = np.array(mom)
std = np.array(std)

plt.scatter(num_frame,mom,marker='x',color='black',label='MOM')
plt.scatter(num_frame,std,marker='v',color='gray',label='SDOM')
plt.xlabel('Number of Frames')
plt.ylabel('Counts/second (ADU/sec)')
plt.legend(loc='best')
plt.savefig('../plots/mom_sdom.png')
plt.show()

