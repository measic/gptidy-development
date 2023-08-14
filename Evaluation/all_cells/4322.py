filename = 'gs://sarasmaster/kopari/shopify/products/products_1.json'
datasetid = 'kopari'
tablename = 'shopify_products'
delimitertype = 'NEWLINE_DELIMITED_JSON'
loadtype = 'WRITE_TRUNCATE'
loadfiletobigquery(filename, datasetid, tablename, delimitertype, loadtype, None)