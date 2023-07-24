wb_list = df_step1.VISS_EU_CD.unique()
print('number of waterbodies in step 1: {}'.format(len(wb_list)))
typeA_list = [row.split('-')[0].strip().lstrip('0') for row in df_step1.WATER_TYPE_AREA.unique()]
print('number of type areas in step 1: {}'.format(len(typeA_list)))