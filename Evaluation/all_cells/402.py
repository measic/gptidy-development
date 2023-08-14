X = np.linspace(-1,1,256)
plt.plot(X+0.5,-Hart(X,1)[1]+0.5,"k-",label= "H = 1")
#plt.plot(X+0.5,-Hart(X,10)[1]+0.5,"b-",label= "H = 10")
#plt.plot(X+0.5,-Hart(X,0.1)[1]+0.5,"r-",label= "H = 0.1")
plt.xlabel("z")
plt.ylabel("$B_{x}$")
plt.title("Campo magnetico Hartmann")
plt.grid(True)
plt.legend()
plt.savefig("Magnetico_Hartmann")