def convert_column_string_encoding(column):
    column = Column([pcc.utils.b(x) for x in column.data], name=column.name)
    return column

def function_def(sn):
    v = sn.lcfit.spline['BessellV']
    mjd_spline = np.arange(np.nanmin(sn.phot.data['BessellV']['MJD']), np.nanmax(sn.phot.data['BessellV']['MJD']), 0.001)
    w = np.where(v(mjd_spline) == np.nanmax(v(mjd_spline)))
    mjdmax = mjd_spline[w]
    return mjdmax