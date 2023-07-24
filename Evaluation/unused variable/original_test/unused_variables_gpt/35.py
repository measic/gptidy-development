import time
tuning_job_name = "forecast-tuning-{}".format(datetime.now().strftime("%d%H%M"))

smclient = boto3.client('sagemaker')
smclient.create_hyper_parameter_tuning_job(HyperParameterTuningJobName=tuning_job_name,
                                           HyperParameterTuningJobConfig=tuning_job_config,
                                           TrainingJobDefinition=training_job_definition)
status = smclient.describe_hyper_parameter_tuning_job(HyperParameterTuningJobName=tuning_job_name)['HyperParameterTuningJobStatus']
print(status)
while status != 'Completed' and status != 'Failed':
    time.sleep(60)
    status = smclient.describe_hyper_parameter_tuning_job(HyperParameterTuningJobName=tuning_job_name)['HyperParameterTuningJobStatus']
    print(status)