# Remove occations with not enough samples
# Or use count as a flag for what to display for the user?
by_date['all_ok'] = True
ix = by_date.loc[by_date['number_of_values'] < 1, 'all_ok'].index
by_date.set_value(ix, 'all_ok', False)