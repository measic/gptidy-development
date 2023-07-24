rmean = numpy.mean(rho)
vmean = (vmax*(1-rmean/rhomax))*(5/18)
print('The Average velocity at t=3 minutes is',"%.2f" %vmean,'m/s')