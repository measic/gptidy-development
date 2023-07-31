data = Table.read("/Users/berto/projects/LSST/cadence/LSST_DDF_2786_cadence.dat", format="ascii.commented_header")
mjd_to_sim = data[np.logical_or(data["filter"] == "LSST_g", data["filter"] == "LSST_r")]["MJD"].data
filters_to_sim = convert_column_string_encoding(data[np.logical_or(data["filter"] == "LSST_g", data["filter"] == "LSST_r")]["filter"]).data