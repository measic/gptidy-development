df['Hotel_Count'] = df.groupby('Hotel Name')['Hotel Name'].transform('count')
descending_hotels = df.sort_values(by=['Hotel_Count'], ascending=False).reset_index()
variable_def = descending_hotels['Hotel Name'].unique()[:150]
most_common_hotels = descending_hotels[descending_hotels['Hotel Name'].isin(variable_def)]