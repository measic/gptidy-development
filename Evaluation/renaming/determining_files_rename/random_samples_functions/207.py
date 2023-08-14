from scipy.integrate import simps

def calc_spectrum_filter_flux(filter_name, SpecClass):
    filter_object = pcc.functions.load_filter('/Users/berto/Code/CoCo/data/filters/' + filter_name + '.dat')
    filter_object.resample_response(new_wavelength=SpecClass.wavelength)
    filter_area = simps(filter_object.throughput, filter_object.wavelength)
    transmitted_spec = filter_object.throughput * SpecClass.flux
    integrated_flux = simps(transmitted_spec, SpecClass.wavelength)
    return integrated_flux / filter_area

def function_def(sn, filtername):
    specphot = np.array([])
    specepoch = np.array([])
    for spec in sn.mangledspec:
        specphot = np.append(specphot, calc_spectrum_filter_flux(filtername, sn.mangledspec[spec]))
        specepoch = np.append(specepoch, sn.mangledspec[spec].mjd_obs)
    return (specepoch, specphot)

def compare_phot_specphot(sn, filtername):
    """"""
    specepoch, specphot = function_def(sn, filtername)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(specepoch, specphot, label='specphot')
    ax.scatter(sn.phot.data[filtername]['MJD'], sn.phot.data[filtername]['flux'], label=filtername)
    ax.set_ylim(0, 1.05 * np.nanmax(np.append(sn.phot.data[filtername]['flux'], specphot)))
    ax.legend()