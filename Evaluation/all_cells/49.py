print ("Writing CSV data for dates {} to {}".format (from_date, until_date))

chunk_size = 100000
print ("Writing {} training records".format (train_df.shape[0]))
for chunk_index in range (0, train_df.shape[0], chunk_size):
    train_df[chunk_index:chunk_index + chunk_size].to_csv(train_output_folder + '/{}-{}_{}-{}.csv'.format (from_date, until_date, chunk_index, chunk_index + chunk_size), header=False, index=False)
    print ("Wrote training records {} to {}".format (chunk_index, chunk_index + chunk_size))

print ("Writing {} validation records".format (validate_df.shape[0]))
for chunk_index in range (0, validate_df.shape[0], chunk_size):
    validate_df[chunk_index:chunk_index + chunk_size].to_csv(validate_output_folder + '/{}-{}_{}-{}.csv'.format (from_date, until_date, chunk_index, chunk_index + chunk_size), header=False, index=False)
    print ("Wrote validation records {} to {}".format (chunk_index, chunk_index + chunk_size))
print ("Export to CSV complete")