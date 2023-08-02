variable_def = ['arr_port', 'pax']
dataframe = get_df_cols(BOOKINGS, variable_def, '^')
print_top_n_arrival_airport(dataframe, 10)