sn_fake = pcc.classes.SNClass("SN2007uy_sim")

sn_fake.load_phot(path = "/Users/berto/projects/LSST/cadence/SN2007uy_sim_LSST_gr.dat")
sn_fake.plot_lc(multiplot = False)