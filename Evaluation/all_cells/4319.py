#Pass bigquery.SourceFormat.NEWLINE_DELIMITED_JSON for JSON in delimiter type and bigquery.SourceFormat.CSV for CSV
def loadfiletobigquery(file_name, dataset_id, table_name, delimitertype, loadtype, skipheader):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_name)
    job_config = bigquery.LoadJobConfig()
    if skipheader is not None:
        job_config.skip_leading_rows = skipheader
    job_config.source_format = delimitertype
    if delimitertype == bigquery.SourceFormat.CSV:
        job_config.autodetect = True
    job_config.write_disposition = loadtype

    load_job = client.load_table_from_uri(
        file_name,
        table_ref,
        job_config=job_config)  # API request

    assert load_job.job_type == 'load'

    load_job.result()  # Waits for table load to complete.

    assert load_job.state == 'DONE'