sn.plot_lc(["BessellV"], multiplot = False)
plt.scatter(p.data["BessellV"]["MJD"], p.data["BessellV"]["flux"], label = "Synthetic Bessell V")
