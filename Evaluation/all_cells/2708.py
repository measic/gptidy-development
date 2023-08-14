arcpy.env.workspace = os.path.join(PATH, 'SF_vote_2016.gdb')

NO_TOUCH = ['OBJECTID', 'precinctname', 'reportingtype', 'precinctid']
FLOAT = ['turnout_percent']

for table in sorted(arcpy.ListTables()):
    for field in arcpy.ListFields(table):
        if field.name not in NO_TOUCH:
            original_name = field.name
            temp_name = field.name[:5] + '_temp'
            arcpy.AddField_management(table, temp_name, 'FLOAT' if original_name in FLOAT else 'LONG')
            arcpy.CalculateField_management(table, temp_name, u'!{}!'.format(original_name), "PYTHON_9.3")
            arcpy.DeleteField_management(table, original_name)
            arcpy.AlterField_management(table, temp_name, to_appropriate_column_name(original_name[:31]))
    print('{} complete'.format(table))