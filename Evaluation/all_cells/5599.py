p = pcc.classes.PhotometryClass()

p.load_table(pcc.utils.simulate_out_to_ap_table(mjd_to_sim, flux, flux_err, filters_to_sim))

# plt.scatter(p.data["BessellV"]["MJD"], p.data["BessellV"]["flux"], label = "Synthetic Bessell V")
plt.scatter(p.data["LSST_g"]["MJD"], p.data["LSST_g"]["flux"], label = "Synthetic LSST g")
plt.scatter(sn.phot.data["BessellV"]["MJD"], sn.phot.data["BessellV"]["flux"], label = "Real Bessell V")
plt.scatter(specphot[0] + mjdmax, specphot[1])

plt.ylim(0, 1.02 *np.nanmax(np.append(p.data["LSST_g"]["flux"], sn.phot.data["BessellB"]["flux"])))
plt.legend()