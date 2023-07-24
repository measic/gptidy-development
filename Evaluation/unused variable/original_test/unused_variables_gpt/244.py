for n in range(1, nt):
    rn = rho.copy()
    
    for j in range(1, nx):
        v = (vmax * (1 - rho / rhomax)) * (5 / 18)
        f1 = v * rho
        rho[1:] = rn[1:] - dt / dx * (f1[1:] - f1[0:-1])
        rho[0] = 20