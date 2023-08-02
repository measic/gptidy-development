def function_def(column_name):
    sql = '\nSELECT\n  {0},\n  COUNT(1) AS num_babies,\n  AVG(weight_pounds) AS avg_wt\nFROM\n  publicdata.samples.natality\nWHERE\n  year > 2000\nGROUP BY\n  {0}\n    '.format(column_name)
    return bq.Query(sql).execute().result().to_dataframe()