agg_methods = {
    'SupDist': 'MIN',
    'BARTDist': 'MIN',
    'AssemDist': 'MIN',
    'CongDist': 'MIN',
    'NeighRep': 'MIN',
    'PREC_2012': 'MIN',
    'PREC_2010': 'MIN',
    'DISTRICT': 'MIN',
    'american_indian_and_alaska_native': 'SUM',
    'asian': 'SUM',
    'black_or_african_american': 'SUM',
    'hispanic_or_latino': 'SUM',
    'native_hawaiian_and_other_pacific_islander': 'SUM',
    'one_race_total': 'SUM',
    'some_other_race': 'SUM',
    'total_population': 'SUM',
    'total_population_not_hispanic_or_latino': 'SUM',
    'two_or_more_races': 'SUM',
    'white': 'SUM'
}


if OVERWRITE:
    arcpy.Delete_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_precinct'))
arcpy.Statistics_analysis(
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_block'),
    os.path.join(PATH, 'derived_data.gdb', 'pop_by_precinct'),
    agg_methods.items(),
    'precinct_id'
)

for field in arcpy.ListFields(os.path.join(PATH, 'derived_data.gdb', 'pop_by_precinct')):
    if field.name[:4] in ('SUM_', 'MIN_'):
        arcpy.AlterField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_precinct'), field.name, field.name[4:35])
arcpy.AlterField_management(os.path.join(PATH, 'derived_data.gdb', 'pop_by_precinct'), 'FREQUENCY', 'num_blocks')