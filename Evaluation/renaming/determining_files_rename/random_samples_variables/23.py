N = Ngenres * Nclips * Nframes * 2
sizeX = N * n / 2.0 ** 20
sizeZ = N * m / 2.0 ** 20
sizeD = n * m / 2.0 ** 10
variable_def = m * n / 2.0 ** 10
print('Size X: {:.1f} M --> {:.1f} MiB'.format(sizeX, sizeX * 4))
print('Size Z: {:.1f} M --> {:.1f} MiB'.format(sizeZ, sizeZ * 4))
print('Size D: {:.1f} k --> {:.1f} kiB'.format(sizeD, sizeD * 4))
print('Size E: {:.1f} k --> {:.1f} kiB'.format(variable_def, variable_def * 4))