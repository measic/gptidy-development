def get_df_cols(csvfilename, cols, separator):
    """
  Method to get a dataframe from a csv file with specified columns
  
  @csvfilename : the name of the file to convert in dataframe
  @cols        : list of string giving columns name to keep
  @separator   : character used to delimit fields in the csv file
  
  @return      : a dataframe
  """
    dataframe = pd.read_csv(BOOKINGS, error_bad_lines=False, encoding='UTF8', sep=separator, usecols=cols)
    return dataframe

def function_def(IATA_code):
    """
    Function to return the name of the airport linked to IATA_code
    
    @IATA_code : String object which is a IATA_code
   
    @return    : String object which is the name of the airport
  """
    try:
        result = GEO_O.get(IATA_code.replace(' ', ''), 'name')
    except KeyError as e:
        result = 'NOT FOUND IATA CODE'
    return result

def get_airports_arrival_sorted(dataframe):
    """
  Method to print the get arrivals airports in 2013 from searches file
  
  @dataframe : the dataframe containing the data
  
  @return    : a new dataframe
  """
    result_dataframe = dataframe.groupby(['arr_port']).sum()
    result_dataframe = result_dataframe.sort_values(by=['pax'], ascending=False)
    return result_dataframe

def add_airports_name(dataframe):
    """
  Method to add a column in a dataframe containing the full name of airports
  thanks to the IATA CODE
  
  @dataframe : the dataframe to modify
  
  @return    : the dataframe modified
  """
    dataframe = dataframe.reset_index()
    dataframe['airport_name'] = dataframe['arr_port'].apply(lambda x: function_def(x))
    return dataframe

def print_top_n_arrival_airport(dataframe, n):
    """
  Method to print the top n of arrival airports in 2013
  
  @dataframe : the preformatted dataframe by columns containing the data
  @n         : the number of airports to show
  """
    df = get_airports_arrival_sorted(dataframe)
    df = add_airports_name(df)
    print(df.head(n))