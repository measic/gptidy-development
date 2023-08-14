plt.figure(figsize=(20,10))

plt.subplot(2, 1, 1)   #パレットを2行1列に分割し，1行目に以下のグラフをプロットする
plt.plot(df['u1_z']/100)   #100で割るのはu1_zの単位が 10^-2deg/s だから
plt.xlabel('time [ms]')    #x軸ラベル
plt.ylabel('u1_z [deg/sec]')    #y軸ラベル
plt.grid()   #プロット領域にグリッド線をつける

plt.subplot(2, 1, 2)   #パレットを2行1列に分割し，2行目に以下のグラフをプロットする
plt.plot(df['u2_z']/100)
plt.xlabel('time [ms]')
plt.ylabel('u2_z [deg/sec]')
plt.grid()