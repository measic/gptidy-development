x = numpy.linspace(0,L,nx)
rho = numpy.ones(nx)*10
rho[10:20] = 50
#rho.min()
pyplot.plot(x,rho, color='red',ls='--', lw=3)
pyplot.ylim(0,52)
#print(rho)