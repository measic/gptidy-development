data_after_subset_filter = lv_workspace.get_filtered_data(level=1, subset='A') # level=0 means first filter 
print('{} rows mathing the filter criteria'.format(len(data_after_subset_filter)))
data_after_subset_filter.head()