unique_hotels_names = variable_def['Hotel Name'].unique()
unique_checkins = variable_def['Checkin Date'].unique()
unique_discount_code = [1, 2, 3, 4]
import itertools
import sys
combs = []
for x in unique_hotels_names:
    for y in unique_checkins:
        for z in unique_discount_code:
            combs.append([x, y, z, sys.maxsize])
new_df = DataFrame.from_records(combs, columns=['Hotel Name', 'Checkin Date', 'Discount Code', 'Discount Price'])
variable_def = variable_def.append(new_df)