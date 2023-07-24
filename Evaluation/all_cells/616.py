from scipy.optimize import curve_fit

bigOccurences = [  0, 244, 777, 523, 576, 693, 643, 674, 463, 326, 178, 107,  97,  56,  54,  55,  58,  57,
  94, 149, 214, 352, 488, 164,   6,   0,   0,   0,   0] # Histogram collected in Big Data Colleciton file
bigMagnitudes = np.linspace(-7, 7, 29)