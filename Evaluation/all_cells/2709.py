if OVERWRITE:
    arcpy.Delete_management(os.path.join(PATH, 'source_data.gdb'))
    arcpy.Delete_management(os.path.join(PATH, 'derived_data.gdb'))
arcpy.CreateFileGDB_management(PATH, 'source_data.gdb')
arcpy.CreateFileGDB_management(PATH, 'derived_data.gdb')
arcpy.FeatureClassToGeodatabase_conversion(
    [
        os.path.join(PATH, 'source_data', 'Census 2010- Blocks for San Francisco', 'geo_export_72486aab-d116-414f-895d-9a7fbaa2a42c.shp'),
        os.path.join(PATH, 'source_data', '2012lines', '2012lines', 'SF_DOE_Precincts_20120702.shp'),
        os.path.join(PATH, 'source_data', '2012lines', '2012lines', 'SF_BOS_20120702_nowater.shp'),
    ],
    os.path.join(PATH, 'source_data.gdb'))
arcpy.TableToGeodatabase_conversion(
    os.path.join(PATH, 'derived_data', 'SF_2010_pop_block.cv'),
    os.path.join(PATH, 'derived_data.gdb')
)

# We don't use a field mapping here because we actually want all the fields from both the target and join inputs
arcpy.SpatialJoin_analysis(
    os.path.join(PATH, 'source_data.gdb', 'geo_export_72486aab_d116_414f_895d_9a7fbaa2a42c'),
    os.path.join(PATH, 'source_data.gdb', 'SF_DOE_Precincts_20120702'),
    os.path.join(PATH, 'derived_data.gdb', 'blocks_join_precincts'),
    match_option='WITHIN',
)

# Since some blocks don't fit in a precicnt, we at least want them to have a distict

fms = arcpy.FieldMappings()
for field in arcpy.ListFields(os.path.join(PATH, 'derived_data.gdb', 'blocks_join_precincts')):
    if field.name.lower() == 'shape':
        continue
    map = arcpy.FieldMap()
    map.addInputField(os.path.join(PATH, 'derived_data.gdb', 'blocks_join_precincts'), field.name)
    fms.addFieldMap(map)
map = arcpy.FieldMap()
map.addInputField(os.path.join(PATH, 'source_data.gdb', 'SF_BOS_20120702_nowater'), 'DISTRICT')
fms.addFieldMap(map)

arcpy.SpatialJoin_analysis(
    os.path.join(PATH, 'derived_data.gdb', 'blocks_join_precincts'),
    os.path.join(PATH, 'source_data.gdb', 'SF_BOS_20120702_nowater'),
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'),
    match_option='WITHIN',
    field_mapping=fms
)

arcpy.AlterField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'), 'Join_Count', 'join_count_precinct')
arcpy.AlterField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'), 'Join_Count_1', 'join_count_district')
arcpy.Delete_management(os.path.join(PATH, 'derived_data.gdb', 'blocks_join_precincts'))