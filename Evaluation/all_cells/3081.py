plt.bar(['knn', 'dt'], [knn_mae, dt_mae])
plt.title('Comparing Mean Absolute Error')
plt.xlabel('algorithm')
plt.ylabel('M.A.E')
plt.show()