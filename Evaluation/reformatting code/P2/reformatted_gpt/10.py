# Find x and y coordinates from Easting and Northing values for the LSOA
a = PM25.attrs['affine']
a = rasterio.Affine.from_gdal(*a)
~a * (439040, 115775)