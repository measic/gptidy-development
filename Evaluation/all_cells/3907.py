#PRINT THE TOP TEN
cols = ["arr_port","pax"]

dataframe = get_df_cols(BOOKINGS,cols,'^')

print_top_n_arrival_airport(dataframe,10)