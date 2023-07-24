trips = bq.Query(afewrecords2, EVERY_N=100000).to_dataframe()
trips[:10]