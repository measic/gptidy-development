plt.figure(figsize=(12,12))

plt.subplot(2, 2, 1)
rv_plot(alpha, u1_z, 8000, 9000, title='thigh (up single stair)')

plt.subplot(2, 2, 2)
rv_plot(alpha, u1_z, 22000, 23000, title='thigh (down single stair)')

plt.subplot(2, 2, 3)
rv_plot(alpha, u1_z, 56000, 58000, title='thigh (up double stair)')

plt.subplot(2, 2, 4)
rv_plot(alpha, u1_z, 66000, 68000, title='thigh (down double stair)')