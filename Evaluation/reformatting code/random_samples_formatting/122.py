plt.figure(figsize=(20,10))

plt.subplot(2, 1, 1)   #パレットを2行1列に分割し，1行目に以下のグラフをプロットする
plt.plot(u1_z)
plt.xlabel('time[ms]')
plt.ylabel(f'u1_z [deg/sec]')
plt.grid()

plt.subplot(2, 1, 2)   #パレットを2行1列に分割し，2行目に以下のグラフをプロットする
plt.plot(u2_z)
plt.xlabel('time[ms]')
plt.ylabel('u2_z [deg/sec]')
plt.grid()