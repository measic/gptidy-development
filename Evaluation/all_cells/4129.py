def rv_plot(r, v, t0, t1, epsilon=500, title='', redrange=None):
    #rとvはそれぞれ対応するarray, t0とt1は第１と第２の極小値近傍時刻, itimeオプションは後のため
    ti = t0 - epsilon
    tf = t1 + epsilon
    tm = ti + (tf - ti) // 2    #tm は ti ~ tf の中間インデックス
    xi = np.where(r==np.min(r[ti:tm]))[0][0]    #xi は ti ~ tm までの r の最小値のインデックス
    xf = np.where(r==np.min(r[tm:tf]))[0][0]    #xf は tm ~ tf までの r の最小値のインデックス
    xm = xi + (xf - xi) // 2    #xm は xi ~ xf の中間インデックス
    plt.plot(r[xi:xm], v[xi:xm], c='black')
    plt.plot(r[xm:xf], v[xm:xf], c='gray')
    ##### ここから #####
    if redrange != None:
        plt.plot(r[redrange[0]:redrange[1]], v[redrange[0]:redrange[1]], c='red', lw=3) #指定個所に赤い曲線を上描き
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms',  f'{redrange[0]}-{redrange[1]}ms'])
    ##### ここまでは後のために #####
    else:
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms'])    #すぐ上のコードがあるのでエラーを出さないためにelse内部に書いた
    plt.title(f'{title}')
    plt.xlabel('angle [deg]')
    plt.ylabel('angular velocity [deg/sec]')                                
    plt.grid()