X = np.linspace(-1,1,256)
plt.plot(X+0.5,-Hart(X,1)[0]+0.5,"k-",label= "H = 1")
#plt.plot(X+0.5,-Hart(X,10)[0]+0.5,"b-",label= "H = 10")
#plt.plot(X+0.5,-Hart(X,0.1)[0]+0.5,"r-",label= "H = 0.1")
plt.xlabel("x")
plt.ylabel("$u_{y}$")
plt.title("Perfil Velocidad Hartmann")
plt.grid(True)
plt.legend()
plt.savefig("Perfil_Hartmann")