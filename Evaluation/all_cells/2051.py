plt.plot(train1.index, train1, label='Train')
plt.plot(test1.index, test1, label='Test')
plt.plot(pred1.index, pred1, label='Holt-Winters1')
plt.legend(loc='best')
