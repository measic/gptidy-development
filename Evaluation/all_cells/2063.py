plt.plot(df_per_day_train1.index, df_per_day_train1, label='Train')
plt.plot(df_per_day_test1.index, df_per_day_test1, label='Test')
plt.plot(pred1.index, pred1, label='Holt-Winters1')
plt.legend(loc='best')