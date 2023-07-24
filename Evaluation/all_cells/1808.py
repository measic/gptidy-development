try:
    files = natsorted(os.listdir('data/'))[1:]
except:
    files = os.listdir('data/')
exp_times = np.array([int(f.split('exp')[1]) for f in files])

#combined frames, and combined frames in counts per second
counts, counts_ps = [], []
for exp in exp_times:
    
    #Read frames, subtract combined bias, combine frames
    array3D = readData('data/exp%s/'%(exp))
    bias_sub_3D = [(frame - bias_2D) for frame in array3D]
    array2D = combineFrame(bias_sub_3D)
    
    array2D_cps = array2D/exp
    
    #cut out safe part of image
    cut = Cutout2D(array2D, window[0], window[1]).data
    cut_cps = Cutout2D(array2D_cps, window[0], window[1]).data
    
    counts.append(cut.flatten())
    counts_ps.append(cut_cps.flatten())
    
    #Plot histogram and image & save to .png
    plotAll(cut, sigma=3, exp=exp, show_level=True, save_dir='writeup/plots/')