# Print out data types
def data_types(df):
    for col in df:
        print(col, type(df[col][1]))   