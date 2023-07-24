plt.figure(figsize=(12,12))

plt.subplot(2, 2, 1)
rv_plot(theta, omega, 8000, 9000, title='knee flexion (up single stair)')

plt.subplot(2, 2, 2)
rv_plot(theta, omega, 22000, 23000, title='knee flexion (down single stair)')

plt.subplot(2, 2, 3)
rv_plot(theta, omega, 56000, 58000, title='knee flexion (up double stair)')

plt.subplot(2, 2, 4)
rv_plot(theta, omega, 66000, 68000, title='knee flexion (down double stair)')