unique_hotels_names = most_checkins["Hotel Name"].unique()
unique_checkins =  most_checkins["Checkin Date"].unique()
unique_discount_code =  [1,2,3,4]

#creating default data - all combination : checking -hotel - discount code
import itertools
import sys
combs = []
for x in unique_hotels_names:
    for y in unique_checkins:
        for z in unique_discount_code:
            combs.append([x, y,z,sys.maxsize])

# converting the default data to data frame and appending to existing
new_df =  DataFrame.from_records(combs,columns=["Hotel Name","Checkin Date","Discount Code","Discount Price"])
most_checkins = most_checkins.append(new_df)