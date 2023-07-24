winkel=np.linspace(20,150,1000)

fig, ax=plt.subplots(dpi=144)
ax.errorbar(anglesA, meanIA ,label="Data A: Expected 35 nm ",xerr=1,yerr=dmeanIA, marker="",ls="",lw=1)
ax.errorbar(angles, meanI ,label="Data B: Expected 180 nm",xerr=1,yerr=dmeanI, marker="",ls="",lw=1)

ax.plot(winkel,formfaktor(winkel,35e-9,100),label="Example: {:.2f} nm".format(35))
ax.plot(winkel,formfaktor(winkel,180e-9,70),label="Example: {:.2f} nm".format(180))

ax.set(xlabel=r"Angle $\theta \: [°]$", ylabel="Form factor $P(q)$", title="Comparison of Data and Expected Radii",
       yscale="log",ylim=[1e-1,150])
ax.legend(frameon=False)
fig.savefig("Plots/Comparison.png")