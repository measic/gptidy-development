# There are many options for reading/writing DataFrames
# e.g. writing a tab delimited file (sep) with no index in the first column and no column title
dfnew.to_csv('mydata.txt', sep='\t', index=False, header=False)