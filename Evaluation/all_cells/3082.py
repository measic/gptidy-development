plt.bar(['knn', 'dt'], [knn_grid_score, dt_grid_score], label='R-Squared', color='coral')
plt.title('Comparing R-Squared Scores')
plt.xlabel('algorithm')
plt.ylabel('R-Squared')
plt.show()