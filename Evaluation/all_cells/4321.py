datasetid = 'kopari'
tablename = 'shopify_products'
client = bigquery.Client()
table_ref = client.dataset(datasetid).table(tablename)
print(table_ref)