X = np.linspace(-1,1,256)
Xp = np.linspace(-1,1,32)
plt.plot(0.5*X + 0.5,Hart(X,1)[1],"k-",label= "H = 1")
plt.plot(0.5*Xp + 0.5,Hart(Xp,1)[1],"b.",label= "H = 1")