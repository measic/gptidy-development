round1_slope_density, round1_slope_value = kde_fit(r1['slp_deg_co'].astype(np.double))
round2_slope_density, round2_slope_value = kde_fit(r2['slp_deg_co'].astype(np.double))

round1_area_density, round1_area_value = kde_fit(r1['flowacc_co'].astype(np.double))
round2_area_density, round2_area_value = kde_fit(r2['flowacc_co'].astype(np.double))
