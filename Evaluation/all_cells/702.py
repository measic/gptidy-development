plt.figure(figsize=(8,8))
for user in users:
    plt.plot(test_loss[user])
plt.title("Custo por época")
plt.show()