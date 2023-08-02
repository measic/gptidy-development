def rv_plot2(r1, v1, r2, v2, t0, t1, epsilon=500, title1='', title2='', redrange=None):
    #0. r1とv2はそれぞれ対応する膝屈曲角とそれの角速度, t0とt1は第１と第２の極小値近傍時刻, itimeオプションは後のため
    ti = t0 - epsilon
    tf = t1 + epsilon
    tm = ti + (tf - ti) // 2    #tm は ti ~ tf の中間インデックス
    xi = np.where(r1==np.min(r1[ti:tm]))[0][0]    #xi は ti ~ tm までの r の最小値のインデックス
    xf = np.where(r1==np.min(r1[tm:tf]))[0][0]    #xf は tm ~ tf までの r の最小値のインデックス
    xm = xi + (xf - xi) // 2    #xm は xi ~ xf の中間インデックス
    
    #1. 膝屈曲角プロット
    plt.subplot(1, 2, 1)
    plt.plot(r1[xi:xm], v1[xi:xm], c='black')
    plt.plot(r1[xm:xf], v1[xm:xf], c='gray')
    if redrange != None:
        plt.plot(r1[redrange[0]:redrange[1]], v1[redrange[0]:redrange[1]], c='red', lw=3) #指定個所に赤い曲線を上描き
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms',  f'{redrange[0]}-{redrange[1]}ms'])
    else:
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms'])    #すぐ上のコードがあるのでエラーを出さないためにelse内部に書いた
    plt.title(f'{title1}')
    plt.xlabel('angle [deg]')
    plt.ylabel('angular velocity [deg/sec]')                                
    plt.grid()
    
    #2. 大腿(下腿)傾き角プロット
    plt.subplot(1, 2, 2)
    plt.plot(r2[xi:xm], v2[xi:xm], c='black')
    plt.plot(r2[xm:xf], v2[xm:xf], c='gray')
    if redrange != None:
        plt.plot(r2[redrange[0]:redrange[1]], v2[redrange[0]:redrange[1]], c='red', lw=3) #指定個所に赤い曲線を上描き
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms',  f'{redrange[0]}-{redrange[1]}ms'])
    else:
        plt.legend([f'{xi}-{xm}ms', f'{xm}-{xf}ms'])    #すぐ上のコードがあるのでエラーを出さないためにelse内部に書いた       
    plt.title(f'{title2}')
    plt.xlabel('angle [deg]')
    plt.ylabel('angular velocity [deg/sec]')                                
    plt.grid()