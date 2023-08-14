# We create tables that will contains every canton we find, so we'll be able to match it with the dataframe at the end.
logger.debug('Beginning of geolocation : creating canton tables')
canton_shortname_table = [] # eg: VD
canton_longname_table = []# eg: Vaud

# number of rows analysed. Can be limited for debuging (eg : 10) because the number of requests to Google Maps API is limited !
MAX_ROWS = math.inf # values between 0 and math.inf 
row_counter = 0 # will be incremented each time we iterate over a row

# maximum duration of a query to the geocoder, in seconds
geocoder_timeout = 5

# We're going to use more than one API key if we want to make all the requests !! :@
# Keys are referenced in a table, se we start with the first key:
APIkeynumber = 0

# This function definition makes the geolocator "stubborn" : it uses all the keys that are available and if it gets a timeout error, it just tries again !        
def stubborn_geocode(geolocator, address):
    global APIkeynumber
    
    try:
        geolocator = geopy.geocoders.GoogleV3(api_key=googlemapsapikeys[APIkeynumber])
        return geolocator.geocode(address, region='ch', timeout=geocoder_timeout)
    
    except geopy.exc.GeocoderTimedOut:
        print("Error : the geocoder timed out. Let's try again...")
        return stubborn_geocode(geolocator, address)
    
    except geopy.exc.GeocoderQuotaExceeded:
        print("Error : The given key has gone over the requests limit in the 24 hour period or has submitted too many requests in too short a period of time. Let's try again with a different key...")
        APIkeynumber = APIkeynumber + 1
        
        try:
            print("Trying API key n°" + str(APIkeynumber) + "...")           
            return stubborn_geocode(geolocator, address)
        
        except IndexError:
            print("Error : Out of API keys ! We need to request another API key from Google :(")
            print("When you get a new API key, add it to the json file containing the others keys.")
            # We have to stop there... the error will be raised and the execution stopped.
            raise

    
# Go through the dataframe that contains all universities and institutions
for index, row in p3_grant_export_data.iterrows():
    logger.debug("Iterating over row n°" + str(row_counter) + ":")
    # initialize variables that will contain canton name for the current row
    canton_longname = 'N/A'
    canton_shortname = 'N/A'
    # Check if the university name exists in our index
    university_name = row['University']
    institution_name = row['Institution']
    if university_name in university_canton_dict:
        # The university has already been located. Let's add the canton to the canton table
        if university_canton_dict[university_name]['long_name'] is not None:
            logger.debug('University already exists in dictionary (' + university_canton_dict[university_name]['long_name'] + ')')
        else:
            logger.debug('University already exists in dictionary, but no canton is associated to it (it might be outside Switzerland).')
        
        canton_longname = university_canton_dict[university_name]['long_name']
        canton_shortname = university_canton_dict[university_name]['short_name']
    
    elif institution_name in institution_canton_dict:
        # The institution has already ben located, so we add its canton to the canton table
        logger.debug('University wasn''t found, but institution already exists in dictionary (' + institution_canton_dict[institution_name]['long_name'] + ')')
        
        canton_longname = institution_canton_dict[institution_name]['long_name']
        canton_shortname = institution_canton_dict[institution_name]['short_name']
    
    else:
        # Nor the university neither the institution has been found yet, so we have to geolocate it
        logger.debug(str(university_name) + ' / ' + str(institution_name) + ' not found in dictionaries, geolocating...')
        adr = stubborn_geocode(geolocator, university_name)
        if adr is None:
            # No address has been found for this University. So we have to do the same with Institution           
            adr = stubborn_geocode(geolocator, institution_name)
            
        # Now, the address should have been found, either by locating the university or the institution
        if adr is not None:                 
            # Check if it's a Swiss address and finds the right canton
            try:
                swiss_address = False
                for i in adr.raw['address_components']:
                    if i["types"][0] == "country" and i["long_name"] == "Switzerland":
                        # The address is located in Switerland
                        swiss_address = True
                # So, we go on only if we found a Swiss address. Otherwise, there is no point to continue.
                if swiss_address:
                    for i in adr.raw['address_components']:
                        if i["types"][0] == "administrative_area_level_1":
                            # We found a canton !
                            canton_longname = (i['long_name'])
                            canton_shortname = (i['short_name'])                          
                            break
                
                
            
            except IndexError:
                # I don't know where this error comes from exactly, just debugging... it just comes from this line :
                # if i["types"][0] == "country" and i["long_name"] == "Switzerland":
                # For the moment I assume that the the address doesn't match the requirements, so it should not be located in Switzerland
                # Thus, we just forget it and look for the next address.
                print("IndexError : no canton found for the current row")
                
            except KeyError:
                print("KeyError : no canton found for the current row")
                print("Current item: n°" + str(len(canton_shortname_table)))
                # The address doesn't act as excpected. There are two possibilities :
                # - The address doesn't contain the field related to the canton
                # - The address doesn't contain the field related to the country
                # So we don't consider this address as a Swiss one and we give up with this one.
    
    # Let's add what we found about the canton !
    # If we didn't find any canton for the current university/institution, it will just append 'N/A' to the tables.
    logger.debug("Appending canton to the table: " + canton_longname)
    canton_shortname_table.append(canton_shortname)
    canton_longname_table.append(canton_longname)
    
    # We also add it to the university/institution dictionary, in order to limit the number of requests
    university_canton_dict[university_name] = {}
    university_canton_dict[university_name]['short_name'] = canton_shortname
    university_canton_dict[university_name]['long_name'] = canton_longname
    institution_canton_dict[institution_name] = {}
    institution_canton_dict[institution_name]['short_name'] = canton_shortname
    institution_canton_dict[institution_name]['long_name'] = canton_longname
            

    row_counter = row_counter + 1
    if row_counter >= MAX_ROWS:
        print("Maximum number of rows reached ! (" + str(MAX_ROWS) + ")")
        print("Increase the MAX_ROWS variable to analyse more locations")
        print("No limit : MAX_ROWS = maths.inf")
        break
