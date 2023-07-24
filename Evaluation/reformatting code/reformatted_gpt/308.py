import matplotlib.pyplot as plt
import numpy as np

f = np.linspace(0, 3e10, 100)
y_nolm_aer_36 = np.random.rand(100)
y_nolm_hitran = np.random.rand(100)

plt.plot(f / 3e10, y_nolm_aer_36, label='AER 3.6')
plt.plot(f / 3e10, y_nolm_hitran, label='HITRAN')
plt.plot(f / 3e10, ty.physics.planck(f, 300), label='Planck')

plt.ylabel('Radiance')
plt.xlabel('Wavenumber')

l = plt.legend()