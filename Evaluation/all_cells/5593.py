verbose = False
# verbose = True
for i, f in enumerate(filters_to_sim):
    filters_to_sim[i] = f.replace(b"SDSS", b"LSST").replace(b"BessellV", b"LSST_g")
#     filters_to_sim[i] = pcc.utils.b(str(f).replace("BessellV", "LSST_g").replace("SDSS_r", "LSST_r")) 
if verbose:
    print(mjdmax)
    print(mjd_to_sim)
    print(filters_to_sim)