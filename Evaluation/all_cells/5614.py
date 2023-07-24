from matplotlib.ticker import MultipleLocator

filters = ["BessellV", "SDSS_r"]
markers = ["x", "o"]
# filters = ["LSST_g"]

alpha = 1.0
xminorticks = 10

pcc.utils.setup_plot_defaults()

fig = plt.figure(figsize=[8, 4])
fig.subplots_adjust(left = 0.1, bottom = 0.13, top = 0.93,
                right = 0.91, hspace=0, wspace = 0)
## Label the axes
xaxis_label_string = r'$\textnormal{Time, MJD (days)}$'
yaxis_label_string = r'$\textnormal{Flux, erg s}^{-1}\textnormal{\AA}^{-1}\textnormal{cm}^{-2}$'

ax1 = fig.add_subplot(111)
axes_list = [ax1]

for j, filter_key in enumerate(filters):
    plot_label_string = r'$\rm{' + sn.phot.data_filters[filter_key].filter_name.replace('_', '\\_') + '}$'

    ax1.errorbar(sn.phot.data[filter_key]['MJD'], sn.phot.data[filter_key]['flux'],
                 yerr = sn.phot.data[filter_key]['flux_err'],
                 capsize = 0, fmt = markers[j], color = "none",
                 label = plot_label_string, ecolor = pcc.hex['batman'], mec = pcc.hex["batman"],
                 alpha = alpha,)
    ax1.fill_between(sn.lcfit.data[filter_key]['MJD'], sn.lcfit.data[filter_key]['flux_upper'], sn.lcfit.data[filter_key]['flux_lower'],
                     color = pcc.hex["batman"],
                     alpha = 0.8, zorder = 0)

fake_filters = ["LSST_g", "LSST_r"]
for j, filter_key in enumerate(fake_filters):
    plot_label_string_fake = r'$\rm{' + sn_fake.phot.data_filters[filter_key].filter_name.replace('_', '\\_') + ', simulated}$'
    
    ax1.errorbar(sn_fake.phot.data[filter_key]['MJD'], sn_fake.phot.data[filter_key]['flux'],
             yerr = sn_fake.phot.data[filter_key]['flux_err'],
             capsize = 0, fmt = 'o', color = sn_fake.phot.data_filters[filter_key]._plot_colour,
#              capsize = 0, fmt = 'o', color = pcc.hex['LSST_g'],
             label = plot_label_string_fake, ecolor = pcc.hex['batman'], mec = pcc.hex["batman"],
             alpha = alpha)
    
xminorLocator = MultipleLocator(xminorticks)
ax1.spines['top'].set_visible(True)
ax1.xaxis.set_minor_locator(xminorLocator)

plot_legend = ax1.legend(loc = 'upper right', scatterpoints = 1, markerfirst = False,
                  numpoints = 1, frameon = False, bbox_to_anchor=(1., 1.),
                  fontsize = 12.)

ax1.set_ylabel(yaxis_label_string)
ax1.set_xlabel(xaxis_label_string)

ax1.set_xlim(ax1.get_xlim()[0], 54643.724999999999 )
outpath = "/Users/berto/projects/LSST/cadence/SN2007uy_cadence_check_LSSTr_LSSTg"

fig.savefig(outpath + ".png", format = 'png', dpi=500)
