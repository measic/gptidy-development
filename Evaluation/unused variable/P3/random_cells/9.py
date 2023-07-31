cadencepath = "/Users/berto/projects/LSST/cadence/LSST_DDF_2786_cadence.dat"

data = Table.read(cadencepath, format = "ascii.commented_header")
w = np.logical_or(data["filter"] == "LSST_g", data["filter"] == "LSST_r")

mjd_to_sim = data[w]["MJD"].data
filters_to_sim = convert_column_string_encoding(data[w]["filter"]).data