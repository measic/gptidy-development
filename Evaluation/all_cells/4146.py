plt.figure(figsize=(12,12))

plt.subplot(2, 2, 1)
rv_plot(theta, omega, 8000, 9000, redrange=[8625, 8725], title='knee flexion (up single stair)')

plt.subplot(2, 2, 2)
rv_plot(theta, omega, 22000, 23000, redrange=[22010, 22100], title='knee flexion (down single stair)')

plt.subplot(2, 2, 3)
rv_plot(theta, omega, 55585, 57678, redrange=[56625, 56700], title='knee flexion (up double stair)')

plt.subplot(2, 2, 4)
rv_plot(theta, omega, 66316, 68149, redrange=[66475, 66530], title='thigh (down double stair)')