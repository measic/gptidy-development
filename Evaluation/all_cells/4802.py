import matplotlib.pyplot as plt
%matplotlib inline
import json
import numpy as np

with open("pretrain losses - srgan.json") as f:
    data = json.load(f)

print("Pretrain loss: Loaded SRGAN JSON.")

# plot the generator loss values
print("Generator loss")
plt.plot(data['generator_loss'])
plt.show()

print("Mean gan loss :", np.mean(data['generator_loss']))
print("Std gan loss : ", np.std(data['generator_loss']))
print("Min gan loss : ", np.min(data['generator_loss']))

# plot the PSNR loss values
print("PSNR loss")
plt.plot(data['val_psnr'])
plt.show()

print("Mean psnr loss :", np.mean(data['val_psnr']))
print("Std psnr loss : ", np.std(data['val_psnr']))
print("Min psnr loss : ", np.min(data['val_psnr']))