# Loop over features (polygons) in the shapefile
for f in tqdm(feats):
    # Rasterize the polygon into an array
    rasterized_image = features.rasterize([(shape(f['geometry']),1)],
                                          out_shape=out_shape,
                                          transform=new_aff,
                                          fill=0,
                                          all_touched=True)

    # Extract from the xarray where the rasterized polygon is
    region = data.where(rasterized_image == 1)
    
    # Combine x and y into a new dimension called allpoints and calculate the mean over it
    # and then convert to a dataframe with an appropriate name
    res = region.stack(allpoints=['x','y']).mean(dim='allpoints').to_dataframe(name=f['properties']['LSOA11CD'])
    
    # Append to the list of data frames so we can concatenate them all at the end
    dfs.append(res)
    
stats = pd.concat(dfs, axis=1)