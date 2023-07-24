def kde_fit(array):
    dens = sm.nonparametric.KDEUnivariate(array)
    dens.fit(bw=2)#bw = bandwidth; how smooth
    density = dens.density
    value = dens.support
    return density, value

elder_slope_density, elder_slope_value = kde_fit(elderSlope.astype(np.double))
elder_area_density, elder_area_value = kde_fit(elderArea.astype(np.double))
fox_slope_density, fox_slope_value = kde_fit(foxSlope.astype(np.double))
fox_area_density, fox_area_value = kde_fit(foxArea.astype(np.double))