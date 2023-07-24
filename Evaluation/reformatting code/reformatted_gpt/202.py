# Importing ground truth
from scipy.io import loadmat

truth_path = "../BSR/BSDS500/data/groundTruth/train/"
gt = loadmat(truth_path + "{0:d}.mat".format(img_no)) 
gt_seg = gt['groundTruth'][0][1][0, 0][0].astype('int64')

plot_seg_vs_truth(img, gt_seg, img_mcmc_2, img_advi_2)