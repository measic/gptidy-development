import matplotlib.pyplot as plt
%matplotlib inline
import json
import numpy as np

with open("fulltrain losses.json") as f:
    data = json.load(f)

print("Fulltrain loss: Loaded fulltrain JSON")

# plot the discriminator loss values
print("PSNR loss")
plt.plot(data['val_psnr'])
plt.show()

print("Mean psnr loss :", np.mean(data['val_psnr']))
print("Std psnr loss : ", np.std(data['val_psnr']))
print("Min psnr loss : ", np.min(data['val_psnr']))

# plot the discriminator loss values
print("Discriminator accuracy")
plt.plot(data['discriminator_acc'])
plt.show()

print("Mean discriminator loss :", np.mean(data['discriminator_loss']))
print("Std discriminator loss : ", np.std(data['discriminator_loss']))
print("Min discriminator loss : ", np.min(data['discriminator_loss']))

# plot the discriminator loss values
print("Discriminator loss")
plt.plot(data['discriminator_loss'])
plt.show()

print("Mean discriminator loss :", np.mean(data['discriminator_loss']))
print("Std discriminator loss : ", np.std(data['discriminator_loss']))
print("Min discriminator loss : ", np.min(data['discriminator_loss']))


# plot the generator loss values
print("Generator loss")
plt.plot(data['generator_loss'])
plt.show()

print("Mean generator loss :", np.mean(data['generator_loss']))
print("Std generator loss : ", np.std(data['generator_loss']))
print("Min generator loss : ", np.min(data['generator_loss']))