# We can already add the values in our dataframe that won't lead to an address
university_canton_dict['Nicht zuteilbar - NA'] = {'long_name': 'N/A', 'short_name': 'N/A'}  # it means "Not Available" in German!
institution_canton_dict['NaN'] = {'long_name': 'N/A', 'short_name': 'N/A'}
institution_canton_dict['nan'] = {'long_name': 'N/A', 'short_name': 'N/A'}