plt.plot(train2.index, train2, label='Train')
plt.plot(test2.index, test2, label='Test')
plt.plot(pred2.index, pred2, label='Holt-Winters2')
plt.legend(loc='best')
