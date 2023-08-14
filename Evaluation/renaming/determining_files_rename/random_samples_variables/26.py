unique_hotels_names = most_checkins['Hotel Name'].unique()
unique_checkins = most_checkins['Checkin Date'].unique()
unique_discount_code = [1, 2, 3, 4]
import itertools
import sys
variable_def = []
for x in unique_hotels_names:
    for y in unique_checkins:
        for z in unique_discount_code:
            variable_def.append([x, y, z, sys.maxsize])
new_df = DataFrame.from_records(variable_def, columns=['Hotel Name', 'Checkin Date', 'Discount Code', 'Discount Price'])
most_checkins = most_checkins.append(new_df)