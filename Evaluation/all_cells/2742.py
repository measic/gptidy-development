from sklearn.metrics import roc_auc_score
# convert prob and test[response] h2oframes to pandas' frames and then convert them each to numpy array
np_array_prob = prob.as_data_frame().as_matrix()
np_array_test = test[response].as_data_frame().as_matrix()
probInPy = np_array_prob
labeInPy = np_array_test
# compare true scores (test[response]) to probability scores (prob)
roc_auc_score(labeInPy, probInPy)