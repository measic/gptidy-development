r_units = ["GRU","GRU_128", "GRU_256", "GRU_64_64"]


f, ax = plt.subplots(1,4, sharey=True, figsize=(15,5))

for i,r_unit in enumerate(r_units):
    
    ax[i].plot(logs[r_unit]["loss"],label=r_unit + "_tr", color='blue')
    ax[i].plot(logs[r_unit]["val_loss"], ls="dashed", label=r_unit + "_val", color="red")
    ax[i].set_ylabel("Loss")
    ax[i].set_xlabel("Epochs")
    ax[i].legend()

f.suptitle("Loss evolution with respect to epochs")
plt.show()