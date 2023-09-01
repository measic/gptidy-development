cols = ['arr_port', 'pax']
variable_def = get_df_cols(BOOKINGS, cols, '^')
print_top_n_arrival_airport(variable_def, 10)