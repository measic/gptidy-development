hpo_data_folder = 'data/hpo'
train_output_folder = hpo_data_folder +'/train'
validate_output_folder = hpo_data_folder +'/validate'
! mkdir -p {train_output_folder}
! mkdir -p {validate_output_folder}

# Earliest possible date is 2017-06-17
from_date = '2017-09-01'
until_date = '2017-11-30'
dates = list(pd.date_range(from_date, until_date, freq='D').strftime('%Y-%m-%d'))

print ("Reading data for dates {} to {}".format (from_date, until_date))
train_df, validate_df = engineer_date_range (dates)