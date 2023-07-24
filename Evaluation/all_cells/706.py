multi_class_predictions = []
for user in users:
    _, predictions = test_accuracy(user, W[user], b[user])
    multi_class_predictions.append(predictions)
multi_class_predictions = np.array(multi_class_predictions)
multi_class_predictions = np.argmax(multi_class_predictions, axis=0)
multi_class_predictions = [users[c] for c in multi_class_predictions]

accuracy = np.mean([pred_class == test_labels[i] for i, pred_class in enumerate(multi_class_predictions)])
print("Acurácia multiclasse: {}".format(accuracy))    