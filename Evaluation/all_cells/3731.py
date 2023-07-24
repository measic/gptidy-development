control = ApparentMagnitudes.from_fits(path=control_path, extvec=extvec,
                                       mag_names=mag_names, err_names=err_names, 
                                       lon_name="GLON", lat_name="GLAT",
                                       frame="galactic", coo_unit="deg")