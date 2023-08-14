#Note that the probability of the first team winning is returned in the 2nd column of the prediction_probabilities array

log_loss_result = utils.compute_log_loss(y_season.values, prediction_probabilities[:,1] )
log_loss_result