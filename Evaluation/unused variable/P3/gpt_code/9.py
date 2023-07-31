data = Table.read(cadencepath, format = "ascii.commented_header")
np.logical_or(data["filter"] == "LSST_g", data["filter"] == "LSST_r")

data["MJD"].data
convert_column_string_encoding(data["filter"]).data