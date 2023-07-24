# show available waterbodies
lst = data_after_subset_filter.SEA_AREA_NAME.unique()
print('Waterbodies in subset:\n{}'.format('\n'.join(lst)))