for f in tqdm(feats):
    rasterized_image = features.rasterize([(shape(f['geometry']), 1)], out_shape=out_shape, transform=new_aff, fill=0, all_touched=True)
    region = data.where(rasterized_image == 1)
    res = region.stack(allpoints=['x', 'y']).mean(dim='allpoints').to_dataframe(name=f['properties']['LSOA11CD'])
    dfs.append(res)
variable_def = pd.concat(dfs, axis=1)