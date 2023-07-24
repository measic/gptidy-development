# trim out columns not relevant to training
trimmed = merged.drop(columns=['ut', 'time', 'airmass', 'cc_x_err', 'cc_y_err', 'chamt', 'osst', 'outt', 'exptime', 'file', 'focerr', 'fwhm', 'raw_seeing', 'residual_rms', 'seeing', 'wavefront_rms', 'xcen', 'ycen', 'comaerr'])
trimmed = trimmed.dropna()
trimmed.head()