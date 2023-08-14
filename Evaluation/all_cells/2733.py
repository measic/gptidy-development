for i in range(5): 
    gbm = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][i])
    #get the parameters from the Random grid search model and modify them slightly
    params = gbm.params
    new_params = {"nfolds":5, "model_id":None}
    for key in new_params.keys():
        params[key]['actual'] = new_params[key]
    new_model = H2OGradientBoostingEstimator()
    for key in params.keys():
        if key in dir(new_model) and getattr(new_model,key) != params[key]['actual']:
            setattr(new_model,key,params[key]['actual'])
    new_model.train(x = predictors, y = response, training_frame = df)  
    cv_summary = new_model.cross_validation_metrics_summary().as_data_frame()
    print(gbm.model_id)
    print(cv_summary.iloc[1]) ## AUC