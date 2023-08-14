Bx ,By, Bz = Lectura("Bx.dat","By.dat","Bz.dat")
ux ,uy, uz = Lectura("vx.dat","vy.dat","vz.dat")
x, y, z = Lectura("x.dat","y.dat","y.dat")


plt.plot(x,5e3*(Bz[32,:]),"b.",label = "Simulacion")
X = np.linspace(-1,1,256)
plt.plot(0.5*X + 0.5,-Hart(X,1)[1],"k-",label= "H = 0.41")
plt.legend()
plt.title("Campo magnetico Hartmann")
plt.grid(True)
plt.xlabel("$x$")
plt.ylabel("$Bz$")
plt.savefig("Haartmannprofile")
