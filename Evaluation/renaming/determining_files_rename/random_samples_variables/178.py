df['Hotel_Count'] = df.groupby('Hotel Name')['Hotel Name'].transform('count')
variable_def = df.sort_values(by=['Hotel_Count'], ascending=False).reset_index()
df_hotels = variable_def['Hotel Name'].unique()[:150]
most_common_hotels = variable_def[variable_def['Hotel Name'].isin(df_hotels)]