plt.plot(train3.index, train3, label='Train')
plt.plot(test3.index, test3, label='Test')
plt.plot(pred3.index, pred3, label='Holt-Winters3')
plt.legend(loc='best')