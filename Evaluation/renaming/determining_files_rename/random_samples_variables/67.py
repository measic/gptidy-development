import random
random.seed(8675309)
variable_def = np.array(glob('lfw/*/*'))
random.shuffle(variable_def)
print('There are %d total human images.' % len(variable_def))