import matplotlib.pyplot as plt
%matplotlib inline
import json
import numpy as np

with open("pretrain losses - discriminator.json") as f:
    data = json.load(f)

print("Pretrain loss: Loaded discriminator JSON")

# plot the discriminator loss values
print("Discriminator loss")
plt.plot(data['discriminator_loss'])
plt.show()

print("Mean discriminator loss :", np.mean(data['discriminator_loss']))
print("Std discriminator loss : ", np.std(data['discriminator_loss']))
print("Min discriminator loss : ", np.min(data['discriminator_loss']))