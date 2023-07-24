#list(zip(typeA_list, df_step1.WATER_TYPE_AREA.unique()))
indicator_list = ['oxygen','bqi','din_winter','ntot_summer', 'ntot_winter', 'dip_winter', 'ptot_summer', 'ptot_winter', 'biov', 'chl', 'secchi']
for indicator in indicator_list:
    w.apply_indicator_data_filter(step = 2, 
                          subset = subset_uuid, 
                          indicator = indicator)