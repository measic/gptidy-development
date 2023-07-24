# ODR 
import scipy.odr as odr
def formfaktor2(B, winkel):
    a,amp=B[0],B[1]
    q=4*np.pi*n/wavelen * np.sin( winkel *gamma /2)
    return 9 * ( np.sin(q*a) - (q*a)* np.cos(q*a) )**2 /  (q*a)**6 *amp

# Funktion funktioniert für yscale="log" bei ca. a=500nm
angles=[]
meanI=[]
dmeanI=[]

for x in range(2,16):
    name="Data/A/{}.ASC".format(x*10)
    angles.append(x*10)
    data=np.genfromtxt(name,skip_header=16,delimiter="\t",filling_values=-1,comments="\"")
    I=data[183:,1]
    I*=np.sin(gamma*x*10) # Winkelkorrektur
    meanI.append(np.mean(I))
    dmeanI.append(np.std(I))
    
start,stop=0,9

linear = odr.Model(formfaktor2)
mydata = odr.RealData(meanI[start:stop], angles[start:stop], sx=dmeanI, sy=1)
myodr = odr.ODR(mydata, linear, beta0=[1e-9,100])
myoutput = myodr.run()
beta=myoutput.beta
dbeta= myoutput.sd_beta
myoutput.pprint()

plotting=np.linspace(20,150,1000)
fig,ax=plt.subplots(dpi=144)
ax.plot(plotting,formfaktor2(beta,plotting))
ax.plot(angles,meanI,label="data")
ax.set(yscale="log")
ax.legend();