# finding minimum  discount price outa  hotel name - checking date - discount code group and fixing data
most_checkins["Discount Price"]= most_checkins.groupby(['Hotel Name','Checkin Date','Discount Code'])["Discount Price"].transform('min')
most_checkins.drop_duplicates(subset=["Hotel Name","Checkin Date","Discount Code"], inplace=True)
most_checkins.sort_values(by=["Hotel Name","Checkin Date","Discount Code"],ascending=True,inplace=True)
most_checkins['Discount Price'].replace(sys.maxsize, -1, inplace=True)

# taking only needed data
checkin_hotel_discount = most_checkins[["Hotel Name","Checkin Date","Discount Code","Discount Price"]].reset_index()
