if OVERWRITE:
    arcpy.Delete_management(os.path.join(PATH, 'SF_vote_2016.gdb'))
arcpy.CreateFileGDB_management(PATH, 'SF_vote_2016.gdb')
arcpy.TableToGeodatabase_conversion(
    [os.path.join(PATH, 'derived_data', '{}.csv'.format(x)) for x in fixed_names.keys()],
    os.path.join(PATH, 'SF_vote_2016.gdb'))