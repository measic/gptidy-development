print(w.get_filtered_data(step = 2, subset = subset_uuid, water_body = wb, indicator = indicator).MONTH.unique())
print(w.get_filtered_data(step = 2, subset = subset_uuid, water_body = wb, indicator = indicator).DEPH.min(),
        w.get_filtered_data(step = 2, subset = subset_uuid, water_body = wb, indicator = indicator).DEPH.max())
print(w.get_filtered_data(step = 2, subset = subset_uuid, water_body = wb, indicator = indicator).VISS_EU_CD.unique())
w.get_filtered_data(step = 2, subset = subset_uuid, water_body = wb).WATER_TYPE_AREA.unique()