variable_def['Hotel_Count'] = variable_def.groupby(
    'Hotel Name')['Hotel Name'].transform('count')
descending_hotels = variable_def.sort_values(
    by=['Hotel_Count'], ascending=False).reset_index()
df_hotels = descending_hotels['Hotel Name'].unique()[:150]
most_common_hotels = descending_hotels[descending_hotels['Hotel Name'].isin(
    df_hotels)]
