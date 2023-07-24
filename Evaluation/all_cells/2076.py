plt.plot(train4.index, train4, label='Train')
plt.plot(test4.index, test4, label='Test')
plt.plot(pred4.index, pred4, label='Holt-Winters4')
plt.legend(loc='best')