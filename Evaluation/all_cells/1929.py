def get_distinct_values(column_name):
    sql = """
SELECT
  {0},
  COUNT(1) AS num_babies,
  AVG(weight_pounds) AS avg_wt
FROM
  publicdata.samples.natality
WHERE
  year > 2000
GROUP BY
  {0}
    """.format(column_name)
    return bq.Query(sql).execute().result().to_dataframe()