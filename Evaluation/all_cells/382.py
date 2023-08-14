#counting and sorting by common checking_data
most_common_hotels["Checkin_Count"] = most_common_hotels.groupby('Checkin Date')['Checkin Date'].transform('count')
descending_most_common_hotels = most_common_hotels.sort_values(by=['Checkin_Count'],ascending=False).reset_index()

#getting first 40 checkins  
common_checkins_list = descending_most_common_hotels["Checkin Date"].unique()[:40]
most_checkins = descending_most_common_hotels[descending_most_common_hotels['Checkin Date'].isin(common_checkins_list)]
