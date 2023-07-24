precision_score = precision(y, preds, weights=None)
print('Average precision: ', precision_score.numpy())