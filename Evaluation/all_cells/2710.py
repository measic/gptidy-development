# First we have to make a precinct_id column, since PREC_2012 is text
# arcpy.AddField_management(PATH + '\\derived_data.gdb\\pop_by_block', 'precinct_id', 'LONG')
# arcpy.CalculateField_management(PATH + '\\derived_data.gdb\\pop_by_block', 'precinct_id', '!PREC_2012!', "PYTHON_9.3")

# Create join key columns, this shit is so jenky
arcpy.AddField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'), 'pop_block_join_key', 'TEXT')
arcpy.CalculateField_management(
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'),
    'pop_block_join_key',
    'str(!tractce10!) + str(!blockce10!)',
    'PYTHON_9.3'
)
arcpy.AddField_management(os.path.join(PATH, 'derived_data.gdb', 'SF_2010_pop_block'), 'pop_block_join_key', 'TEXT')
arcpy.CalculateField_management(
    os.path.join(PATH, 'derived_data.gdb', 'SF_2010_pop_block'),
    'pop_block_join_key',
    "'0' + str(!census_tract!) + str(!block!)",
    'PYTHON_9.3'
)

# Now do the actual join
arcpy.JoinField_management(
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'),
    'pop_block_join_key',
    os.path.join(PATH, 'derived_data.gdb', 'SF_2010_pop_block'),
    'pop_block_join_key'
)

# Also make a precinct_id column, since PREC_2012 is text
arcpy.AddField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'), 'precinct_id', 'LONG')
func = """def to_int(x):
    if sum([a.isalnum() for a in x]) == 0:
        return None
    else:
        return int(x)
    """
arcpy.CalculateField_management(
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'),
    'precinct_id',
    'to_int(!PREC_2012!)',
    'PYTHON_9.3',
    func
)