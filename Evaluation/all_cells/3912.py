# PRINT TOP 10 AIRPORT ARRIVALS
BOOKINGS_GROUP_BY_ARR_PORT.sort_values(by=['pax'], ascending=False).head(10)