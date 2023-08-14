from GeoBases import GeoBase

#IMPORT DATA FROM GEOBASE
geo_o = GeoBase(data='ori_por', verbose=False)


def get_name(IATA_code):
  """
    Function to return the name of the airport linked to IATA_code
    
    @IATA_code : String object which is a IATA_code
   
    @return    : String object which is the name of the airport
  """
  try:
    result = geo_o.get(IATA_code.replace(" ",""), 'name')
  except KeyError as e:
    result = "NOT FOUND IATA CODE"
   
  return result
  


BOOKINGS_GROUP_BY_ARR_PORT.columns.values
new_df = BOOKINGS_GROUP_BY_ARR_PORT.reset_index()

new_df['airport_name'] = new_df['arr_port'].apply(lambda x: get_name(x))

new_df