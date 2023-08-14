## rbind() makes a copy here, so it's better to use split_frame with `ratios = c(0.8)` instead above
cv_gbm = H2OGradientBoostingEstimator(nfolds = 4, seed = 0xDECAF)
cv_gbm.train(x = predictors, y = response, training_frame = train.rbind(valid))