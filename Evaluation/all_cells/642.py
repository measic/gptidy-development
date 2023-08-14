# Specifying the region for the geolocator: for instance, University of Geneva might be localized in the US !
test_geolocator =  geopy.geocoders.GoogleV3(api_key=googlemapsapikeys[0])
test_university_geneva = test_geolocator.geocode("University of Geneva", region='ch')
test_university_geneva