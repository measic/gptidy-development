xi = np.where(theta==np.min(theta[ti:tm]))[0][0]   #np.minは教科書p.129を参照
xf = np.where(theta==np.min(theta[tm:tf]))[0][0]
xm = xi + (xf - xi) // 2
print(f'xi={xi}, xf={xf}, xm={xm}')