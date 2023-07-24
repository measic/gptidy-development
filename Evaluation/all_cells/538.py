def formfaktor(winkel,a,amp=1):
    #winkel=winkel+offset
    q=4*np.pi*n/wavelen * np.sin( winkel *gamma /2)
    
    return 9 * ( np.sin(q*a) - (q*a)* np.cos(q*a) )**2 /  (q*a)**6 *amp

def formfaktorQ(q,a,amp=1):
    return 9 * ( np.sin(q*a) - (q*a)* np.cos(q*a) )**2 /  (q*a)**6 *amp

# Funktion funktioniert für yscale="log" bei ca. a=500nm