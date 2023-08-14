plt.figure(figsize=(20,20))

plt.subplot(4, 1, 1)   #パレットを4行1列に分割し，1行目に以下のグラフをプロットする
plt.plot(u1_z[:14000], c='blue')
plt.plot(u2_z[:14000], c='red')
plt.title('up stairs')
plt.xlabel('time[ms]')
plt.ylabel('angular velocity [deg/sec]')
plt.ylim([-350, 350])
plt.legend(['z1_z', 'z2_z'])
plt.grid()   #プロット領域にグリッド線をつける

plt.subplot(4, 1, 2)   #パレットを4行1列に分割し，2行目に以下のグラフをプロットする
plt.plot(np.arange(14000,28000), u1_z[14000:28000], c='blue')
plt.plot(np.arange(14000,28000), u2_z[14000:28000], c='red')
plt.title('down stairs')
plt.xlabel('time[ms]')
plt.ylabel('angular velocity [deg/sec]')
plt.ylim([-350, 350])
plt.legend(['z1_z', 'z2_z'])
plt.grid()

plt.subplot(4, 1, 3)   #パレットを4行1列に分割し，3行目に以下のグラフをプロットする
plt.plot(np.arange(51000, 63000), u1_z[51000:63000], c='blue')
plt.plot(np.arange(51000, 63000), u2_z[51000:63000], c='red')
plt.title('up stairs')
plt.xlabel('time[ms]')
plt.ylabel('angular velocity [deg/sec]')
plt.ylim([-350, 350])
plt.legend(['z1_z', 'z2_z'])
plt.grid()

plt.subplot(4, 1, 4)   #パレットを4行1列に分割し，4行目に以下のグラフをプロットする
plt.plot(np.arange(63000,75000), u1_z[63000:75000], c='blue')
plt.plot(np.arange(63000,75000), u2_z[63000:75000], c='red')
plt.title('down stairs')
plt.xlabel('time[ms]')
plt.ylabel('angular velocity [deg/sec]')
plt.ylim([-350, 350])
plt.legend(['z1_z', 'z2_z'])
plt.grid()