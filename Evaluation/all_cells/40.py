prefix = 'hpo'
s3_hpo_uri = 's3://{}/{}/'.format (YOUR_BUCKET_NAME, prefix)

!aws s3 mb "s3://{YOUR_BUCKET_NAME}"