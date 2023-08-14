# DATAFRAME STRUCTURE
  BOOKINGS_DF_STRUCT = pd.read_csv(BOOKINGS, error_bad_lines=False, encoding='UTF8', sep='^', nrows=1)

# Dataframe using suggested columns
BOOKINGS_DF_EX = pd.read_csv(BOOKINGS, error_bad_lines=False, encoding='UTF8', sep='^', usecols=['arr_port','pax'])