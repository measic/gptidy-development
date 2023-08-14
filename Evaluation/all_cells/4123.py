plt.figure(figsize=(20,10))

plt.subplot(2, 1, 1)   #パレットを2行1列に分割し，1行目に以下のグラフをプロットする
plt.plot(theta)
plt.title('flexion angle around knee')
plt.grid()

plt.subplot(2, 1, 2)   #パレットを2行1列に分割し，2行目に以下のグラフをプロットする
plt.title('flexion angler velocity around knee')
plt.plot(omega)
plt.grid()