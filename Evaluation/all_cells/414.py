#Bx ,By, Bz = Lectura("Primer_Resultado/Bx.dat","Primer_Resultado/By.dat","Primer_Resultado/Bz.dat")
#ux ,uy, uz = Lectura("Primer_Resultado/vx.dat","Primer_Resultado/vy.dat","Primer_Resultado/vz.dat")
#x, y, z = Lectura("Primer_Resultado/x.dat","Primer_Resultado/y.dat","Primer_Resultado/y.dat")


plt.plot(x,1e13*Bx[18,:],"b.",label = "Simulacion")
X = np.linspace(-1,1,256)
plt.plot(0.5*X + 0.5,-Hart(X,0.43)[1],"k-",label= "H = 0.4")
plt.legend()