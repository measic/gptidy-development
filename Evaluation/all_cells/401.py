def Hart(x,H):
    F = 1.0;L = 1.0;Bo = 1.0;rhoo = 1.0
    eta = 1.0; nu =1.0
    #H = Bo*L/(np.sqrt(rhoo*nu*eta))
    u = (F*L)/(np.sqrt(rhoo*Bo))*np.sqrt(eta/nu)*(1/np.tanh(H))*(1-((np.cosh(H*x/L))/(np.cosh(H)))) 
    b = ((F*L)/(Bo))*(((np.sinh(H*x/L))/(np.sinh(H)))-x/L)
    return [u,b]
    
    
    