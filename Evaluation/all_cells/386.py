#normalizing only positive numbers, ignoring -1 values
discount_filtered = checkin_hotel_discount[checkin_hotel_discount['Discount Price'] > -1 ]

def normalize_data(x):
    diff = max(x) - min(x)
    if(diff == 0):
        return 0
    else:
        return (round( ( x - min(x) ) / ( max(x) - min(x) ) * 100 ))

discount_filtered_grouped = discount_filtered.groupby('Hotel Name')['Discount Price']
discount_filtered["Normal"] = discount_filtered_grouped.transform(normalize_data) 

discount_synth = checkin_hotel_discount[checkin_hotel_discount['Discount Price'] == -1 ]
discount_synth["Normal"] = -1

#checkin_hotel_discount
normal_dataFrame = discount_synth.append(discount_filtered)
normal_dataFrame.sort_values(by=["Hotel Name","Checkin Date","Discount Code"],ascending=True,inplace=True)
normal_dataFrame


# NOTES
# We had an issue with N/A values.
# There were few possiboles reasons for this problem.
# One Posibility is that we had one row per hotel name (the rest were -1 and weren't included in this data frame ) and the calculate of max value less min value gave as zero.
# Another posibility is that all the rows of the hotels were equal and the maximun and minimum value price were equal.
# We solved this issue by checking if the maximum and minimum value of hotel names group by is 0, and return 0 and not calculating and dividing by 0.