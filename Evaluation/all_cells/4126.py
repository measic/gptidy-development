plt.figure(figsize=(20,40))

plt.subplot(8, 1, 1)   #パレットを8行1列に分割し，1行目に以下のグラフをプロットする
plt.plot(theta[:14000])
plt.title('flexion angle around knee (up sigle stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angle [deg]')
plt.grid()

plt.subplot(8, 1, 2)   #パレットを8行1列に分割し，2行目に以下のグラフをプロットする
plt.plot(omega[:14000])
plt.title('flexion angler velocity around knee (up sigle stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angular velocity [deg/s]')
plt.grid()

plt.subplot(8, 1, 3)   #パレットを8行1列に分割し，3行目に以下のグラフをプロットする
plt.plot(np.arange(14000, 28000), theta[14000:28000])
plt.title('flexion angle around knee (down sigle stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angle [deg]')
plt.grid()

plt.subplot(8, 1, 4)   #パレットを8行1列に分割し，4行目に以下のグラフをプロットする
plt.plot(np.arange(14000, 28000), omega[14000:28000])
plt.title('flexion angler velocity around knee (down sigle stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angular velocity [deg/s]')
plt.grid()

plt.subplot(8, 1, 5)   #パレットを8行1列に分割し，5行目に以下のグラフをプロットする
plt.plot(np.arange(52000, 64000), theta[52000:64000])
plt.title('flexion angle around knee (up double stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angle [deg]')
plt.grid()

plt.subplot(8, 1, 6)   #パレットを8行1列に分割し，6行目に以下のグラフをプロットする
plt.plot(np.arange(52000, 64000), omega[52000:64000])
plt.title('flexion angler velocity around knee (up double stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angular velocity [deg/s]')
plt.grid()

plt.subplot(8, 1, 7)   #パレットを8行1列に分割し，7行目に以下のグラフをプロットする
plt.plot(np.arange(63000, 74000), theta[63000:74000])
plt.title('flexion angle around knee (down double stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angle [deg]')
plt.grid()

plt.subplot(8, 1, 8)   #パレットを8行1列に分割し，8行目に以下のグラフをプロットする
plt.plot(np.arange(63000, 74000), omega[63000:74000])
plt.title('flexion angler velocity around knee (down double stairs)')
plt.xlabel('time [ms]')
plt.ylabel('angular velocity [deg/s]')
plt.grid()