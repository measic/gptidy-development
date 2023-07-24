plt.plot(df_per_day_train2.index, df_per_day_train2, label='Train')
plt.plot(df_per_day_test2.index, df_per_day_test2, label='Test')
plt.plot(pred2.index, pred2, label='Holt-Winters2')
plt.legend(loc='best')