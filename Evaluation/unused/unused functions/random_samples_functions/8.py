def Lectura(ux,uy,uz):
    Ux = np.loadtxt(ux, unpack = True)
    Uy = np.loadtxt(uy, unpack = True)
    Uz = np.loadtxt(uz, unpack = True)
    return Ux,Uy,Uz
    


def Grafica(udat,vdat,xdat,ydat,linea):
    uesc = 1.0#dx/dt
    u = np.loadtxt(udat, unpack = True)
    v = np.loadtxt(vdat, unpack = True)
    x = np.loadtxt(xdat, unpack = True)
    y = np.loadtxt(ydat, unpack = True)
    #rho = np.loadtxt(rhodat, unpack = True)
    X = np.linspace(0,1,50)

    f, axarr = plt.subplots(1,2, figsize=(24,6))
    st = f.suptitle("$\\tau = 0.6$", fontsize=25)
    st.set_y(1.0)
    pasos = 12
    M= np.hypot(u, v)
    #axarr[0].streamplot(x,y,u,v, color="k",linewidth=0.8,density=1.0, arrowstyle='->', arrowsize=1.5)
    im=axarr[0].quiver(x,y,u,v,M , cmap=plt.cm.jet,width=0.022,scale=1/0.1)
    axarr[0].set_title("Campos",fontsize = 20)
    axarr[0].set_xlim(-0.01,1)
    axarr[0].set_xlabel("$x[m]$",fontsize = 20)
    axarr[0].set_ylabel("$y[m]$",fontsize = 20)
    axarr[0].tick_params(axis="x", labelsize=20)
    axarr[0].tick_params(axis="y", labelsize=20)
    
    axarr[1].plot(x,v[linea,:],"b", label = "Simulacion")
    #axarr[1].plot(X,uesc*uy(X,nul,gl,Pl),"r+", label = "Teorica")
    #axarr[1].set_ylim(-0.1*uesc,0)
    axarr[1].legend()
    axarr[1].grid(True)
    axarr[1].set_title('Perfil de Velocidad',fontsize = 20,y=1.0)
    axarr[1].set_xlabel("$x[m]$",fontsize = 20)
    axarr[1].set_ylabel("$v[m/s]$",fontsize =20)
    axarr[1].tick_params(axis="x", labelsize=20)
    axarr[1].tick_params(axis="y", labelsize=20)
    
    cbar = f.colorbar(im, ax=axarr, shrink = 1.0)
    cbar.set_label('$v[m/s]$',fontsize =20)
    cbar.ax.tick_params(labelsize=20)
    