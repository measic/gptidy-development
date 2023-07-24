pwf2 = pm.piecewise(preslope=0, breaksxy=[(0, 0), (1000, 400), (3000, 800)], postslope=0.1)
# plot the function
pwf2.plot(lx=-1, rx=4000, k=1, color='r', marker='o', linewidth=2)