#check if image slice looks good on long exposure image
longexp_3D = readData('data/exp768/')
longexp_sub_3D = [(frame - bias_2D) for frame in longexp_3D]
longexp_2D = combineFrame(longexp_sub_3D)

plotImg(longexp_2D, window=window, save_dir='writeup/plots/')