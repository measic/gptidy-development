window = [(550,550), (15,15)]

bias_3D = readData('data/exp0/')
bias_2D = combineFrame(bias_3D)

#cut data
bias_2D_cut = Cutout2D(bias_2D, window[0], window[1]).data

plotAll(bias_2D_cut, sigma=3, exp=0, save_dir='writeup/plots/')