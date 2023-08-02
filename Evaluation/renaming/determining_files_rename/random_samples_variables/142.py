verbose = False
for i, f in enumerate(variable_def):
    variable_def[i] = f.replace(b'SDSS', b'LSST').replace(b'BessellV', b'LSST_g')
if verbose:
    print(mjdmax)
    print(mjd_to_sim)
    print(variable_def)