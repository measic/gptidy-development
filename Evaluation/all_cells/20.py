recall_score = recall(y, preds, weights=None)
print('Average precision: ', recall_score.numpy())