filename = 'gs://sarasmaster/sarasdata/client_shopify_entitlements.csv'
datasetid = 'sarasdata'
tablename = 'client_shopify_entitlements'
delimitertype = 'CSV'
loadtype = 'WRITE_TRUNCATE'
loadfiletobigquery(filename, datasetid, tablename, delimitertype, loadtype, 1)