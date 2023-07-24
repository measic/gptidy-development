prob = None
k = 10
for i in range(0, k):
    gbm = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][i])
    if prob is None:
        prob = gbm.predict(test)["p1"]
    else:
        prob = prob + gbm.predict(test)["p1"]
prob = prob / k