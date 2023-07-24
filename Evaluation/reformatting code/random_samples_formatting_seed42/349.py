water_body = 'SE574000-114230' # type_area 1-s,
w.get_step_object(step = 2, subset = subset_uuid).load_indicator_settings_filters()

temp = w.get_step_object(step = 2, subset = subset_uuid).indicator_data_filter_settings['oxygen']
temp.get_value(variable='REF_VALUE', type_area='1', water_body = water_body)
#temp.settings.df