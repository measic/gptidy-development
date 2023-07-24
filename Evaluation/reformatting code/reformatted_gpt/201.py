# Image to rasterize the polygons into
rasterized_image = np.zeros(data.isel(time=0).shape, dtype=np.int)

# List to store dataframes in
dfs = []

feats = read_features(r'D:\Annies_Dissertation\Data\Boundaries\LSOA_Wessex.shp')

out_shape = data.isel(time=0).shape