import matplotlib.pyplot as plt

plt.scatter(dt_grid.predict(test_features), test_outcome, alpha=0.5, label='DecisionTree')
plt.scatter(knn_grid.predict(test_features), test_outcome, alpha=0.5, label='KNN')
plt.plot(test_outcome, test_outcome, label='y=x', c='green', alpha=0.2)
plt.legend()
plt.ylabel('Actual Delay')
plt.xlabel('Predicted Delay')
plt.title('Predicted v.s. Actual Delay')