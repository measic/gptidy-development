tuning_job_config = {
    "ParameterRanges": {
        "CategoricalParameterRanges": [],
        "ContinuousParameterRanges": [
            {
                "MaxValue": "0.9",
                "MinValue": "0.1",
                "Name": "eta"
            },
            {
                "MaxValue": "2",
                "MinValue": "0",
                "Name": "alpha"
            },
            {
                "MaxValue": "9.0",
                "MinValue": "0.1",
                "Name": "gamma"
            },
            {
                "MaxValue": "10",
                "MinValue": "1",
                "Name": "min_child_weight"
            }
        ],
        "IntegerParameterRanges": [
            {
                "MaxValue": "10",
                "MinValue": "3",
                "Name": "max_depth"
            },
            {
                "MaxValue": "100",
                "MinValue": "10",
                "Name": "num_round"
            }
        ]
    },
    "ResourceLimits": {
        "MaxNumberOfTrainingJobs": 10,
        "MaxParallelTrainingJobs": 3
    },
    "Strategy": "Bayesian",
    "HyperParameterTuningJobObjective": {
        "MetricName": "validation:rmse",
        "Type": "Minimize"
    }
}