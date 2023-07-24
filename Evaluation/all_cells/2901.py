plt.plot(f/3e10, y_nolm_aer, label='AER')
plt.plot(f/3e10, y_lm, label='AER-LM')
plt.plot(f/3e10, ty.physics.planck(f, 300), label='Planck')
plt.ylabel('Radiance')
plt.xlabel('Wavenumber')
l = plt.legend()