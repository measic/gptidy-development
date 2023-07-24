job_config = bigquery.LoadJobConfig()
job_config.schema = [
    bigquery.SchemaField('name', 'STRING'),
    bigquery.SchemaField('post_abbr', 'STRING')
]