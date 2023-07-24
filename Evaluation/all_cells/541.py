angles=[]
meanI=[]
dmeanI=[]

for x in range(2,16):
    name="Data/B/{}.ASC".format(x*10)
    angles.append(x*10)
    data=np.genfromtxt(name,skip_header=16,delimiter="\t",filling_values=-1,comments="\"")
    I=data[183:,1]
    I*=np.sin(gamma*x*10) # Winkelkorrektur
    
    meanI.append(np.mean(I))
    dmeanI.append(np.std(I))
    
fig,ax=plt.subplots(dpi=144)
ax.errorbar(angles, meanI ,label="Data",xerr=1,yerr=dmeanI, marker="",ls="",lw=1)
    
fit_mi_shit(0,-1,60)
fit_mi_shit(0,9,30)
fit_mi_shit(9,-1,100)

"""for i in np.linspace(35e-9,180e-9,2):
    ax.plot(q, formfaktor(q,i,100) ,label="Testwert: {:.2f} nm".format(i/1e-9,popt[0]*1e9,perr[0]*1e9))
"""
q=np.linspace(angles[0],120,1000)
ax.plot(q, formfaktor(q,106e-9,50) ,label="Example: {:.2f} nm".format(106) )
ax.set(xlabel=r"Angle $\theta \: [°]$", ylabel="Form factor $P(q)$", title="Formfactor for Data B",yscale="log")

ax.legend(frameon=False)
fig.savefig("Plots/FormB");