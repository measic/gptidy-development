vmin = (vmax*(1-rho/rhomax))*(5/18)
vn = numpy.min(vmin)
print('The minimum velocity at t=6 minutes is', "%.2f" %vn ,'m/s')