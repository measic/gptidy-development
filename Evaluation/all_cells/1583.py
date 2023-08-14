# Get the actual Affine object from the data stored in the attrs
orig_aff = rasterio.Affine.from_gdal(*data.attrs['affine'])