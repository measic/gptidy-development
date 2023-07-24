r_units = ["RNN", "LSTM", "GRU"]

f, ax = plt.subplots(1,3, sharey=True, figsize=(15,5))

for i,r_unit in enumerate(r_units):
    
    ax[i].plot(logs[r_unit]["acc"],label=r_unit + "_tr", color='blue')
    ax[i].plot(logs[r_unit]["val_acc"], ls="dashed", label=r_unit + "_val", color="red")
    ax[i].set_ylabel("Accuracy")
    ax[i].set_xlabel("Epochs")
    ax[i].legend()

f.suptitle("Accuracy evolution with respect to epochs")
plt.show()