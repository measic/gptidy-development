import scipy.special as ssss
def p(q,a):
    return 9 * ( np.sin(q*a) - (q*a)* np.cos(q*a) )**2 /  (q*a)**6
def gauss(x,m,sig):
    return np.exp(-(x-m)**2/2/sig**2) / np.sqrt(2*np.pi*sig**2)
def integral(q,m,sig):
    results=[]
    for i in range(len(q)):
        q0= q[i]
        def c(a): 
            return p(q0,a) * gauss(a,m,sig)
        results.append(sci.quad(c, 0,np.inf)[0] )
    return results

winkel=np.linspace(20,150,1000)
q=4*np.pi*n/wavelen * np.sin( winkel *gamma /2)

fig,ax=plt.subplots(dpi=144)
ax.plot(winkel,integral(q,60e-9,5e-9),label="r3242")
ax.plot(winkel,p(q,60e-9))
ax.set(yscale="log")
ax.legend();