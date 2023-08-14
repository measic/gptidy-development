import warnings

# evaluate an ARIMA model for a given order (p,d,q)
def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    train = X.loc[:39,['client-ip-unique-count']]
    test= X.loc[40:,['client-ip-unique-count']]
    
    history = [x for x in train]
    # make predictions
    predictions = list()
    model = sm.tsa.ARIMA(train, order=arima_order).fit()
    predictions = model.predict(40,42,dynamic=True)
    error = mean_absolute_error(test, predictions)
    return error


# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mae = evaluate_arima_model(dataset, order)
                    if mae < best_score:
                        best_score, best_cfg = mae, order
                    print('ARIMA%s MAE=%.3f' % (order,mae))
                except:
                    continue
    print('Best ARIMA%s MAE=%.3f' % (best_cfg, best_score))
 

# load dataset
p_values = [0, 1, 2, 4,6,8,10]
d_values = range(0, 3)
q_values = range(0, 3)
warnings.filterwarnings("ignore")
evaluate_models(log_and_placements_aggregated_per_week_df.loc[:,['client-ip-unique-count']], p_values, d_values, q_values)