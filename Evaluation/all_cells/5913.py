# plot the train and validation logp for all three learning rates in one figure
lrs = [1e-2, 1e-3, 1e-4]


plt.figure(figsize=(20,10))
for i in range(len(logp_train)):
    plt.plot(logp_train[i], label=f'Train lr={lrs[i]}')
    plt.plot(logp_valid[i], label=f'Valid lr={lrs[i]}')
plt.title('Log probability of during training on train-set and validation-set for different learning rates')
plt.xlabel('epochs')
plt.ylabel('log probability')
plt.legend()
plt.show()