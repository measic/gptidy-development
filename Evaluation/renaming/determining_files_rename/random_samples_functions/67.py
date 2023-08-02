discount_filtered = checkin_hotel_discount[checkin_hotel_discount['Discount Price'] > -1]

def function_def(x):
    diff = max(x) - min(x)
    if diff == 0:
        return 0
    else:
        return round((x - min(x)) / (max(x) - min(x)) * 100)
discount_filtered_grouped = discount_filtered.groupby('Hotel Name')['Discount Price']
discount_filtered['Normal'] = discount_filtered_grouped.transform(function_def)
discount_synth = checkin_hotel_discount[checkin_hotel_discount['Discount Price'] == -1]
discount_synth['Normal'] = -1
normal_dataFrame = discount_synth.append(discount_filtered)
normal_dataFrame.sort_values(by=['Hotel Name', 'Checkin Date', 'Discount Code'], ascending=True, inplace=True)
normal_dataFrame