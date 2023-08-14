ux ,uy, uz = Lectura("vx.dat","vy.dat","vz.dat")
x, y, z = Lectura("x.dat","y.dat","z.dat")

Grafica("vx.dat","vy.dat","x.dat","y.dat",32)
plt.savefig("velocidad")
Grafica("Bx.dat","Bz.dat","x.dat","y.dat",32)
plt.savefig("Magentico")


