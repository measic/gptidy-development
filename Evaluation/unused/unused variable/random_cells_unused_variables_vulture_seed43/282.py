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

#meanI=[y/np.max(meanI) for y in meanI] # Normierung auf die größte Intensität
#
# WIE SOLL MAN DAS RICHTIG NORMIEREN ???
# 
# Datapoints for fitting
start=9
stop=-1

fig,ax=plt.subplots(dpi=144)
ax.errorbar(angles, meanI ,label="Data",xerr=1,yerr=dmeanI, marker="",ls="",lw=1)

def fit_mi_shit(start,stop,a):
    popt,pcov=cf(formfaktor, angles[start:stop], meanI[start:stop], p0=(200e-9,a))
    perr = np.sqrt(np.diag(pcov))

    q=np.linspace(angles[start],angles[stop],1000)
    ax.plot(q, formfaktor(q,*popt) ,label="Fit: a= {:.2f} $\pm$ {:.2f} nm".format(abs(popt[0])*1e9,abs(perr[0])*1e9))

fit_mi_shit(0,-1,30)
fit_mi_shit(0,9,30)
fit_mi_shit(9,-1,30)

"""for i in np.linspace(35e-9,180e-9,2):
    ax.plot(q, formfaktor(q,i,100) ,label="Testwert: {:.2f} nm".format(i/1e-9,popt[0]*1e9,perr[0]*1e9))
"""
q=np.linspace(angles[0],120,1000)
ax.plot(q, formfaktor(q,113e-9,100) ,label="Example: {:.2f} nm".format(113) )
ax.set(xlabel=r"Angle $\theta \: [°]$", ylabel="Form factor $P(q)$", title="Formfactor for Data A",yscale="log")

ax.legend(frameon=False)
fig.savefig("Plots/FormA");

anglesA,meanIA,dmeanIA = angles,meanI,dmeanI