plt.figure(figsize=(8,8))
for user in users:
    plt.plot(test_accuracies[user])
plt.title("Acurácia por época")
plt.show()