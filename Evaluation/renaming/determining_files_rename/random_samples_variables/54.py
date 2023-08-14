from matplotlib.ticker import MultipleLocator
filters = ['LSST_g']
alpha = 1.0
xminorticks = 10
pcc.utils.setup_plot_defaults()
fig = plt.figure(figsize=[8, 4])
fig.subplots_adjust(left=0.1, bottom=0.13, top=0.93, right=0.91, hspace=0, wspace=0)
xaxis_label_string = '$\\textnormal{Time, MJD (days)}$'
yaxis_label_string = '$\\textnormal{Flux, erg s}^{-1}\\textnormal{\\AA}^{-1}\\textnormal{cm}^{-2}$'
variable_def = fig.add_subplot(111)
axes_list = [variable_def]
for filter_key in filters:
    plot_label_string = '$\\rm{' + sn.phot.data_filters['BessellV'].filter_name.replace('_', '\\_') + '}$'
    plot_label_string_fake = '$\\rm{' + sn_fake.phot.data_filters[filter_key].filter_name.replace('_', '\\_') + ', simulated}$'
    variable_def.errorbar(sn.phot.data['BessellV']['MJD'], sn.phot.data['BessellV']['flux'], yerr=sn.phot.data['BessellV']['flux_err'], capsize=0, fmt='x', color=sn.phot.data_filters['BessellV']._plot_colour, label=plot_label_string, ecolor=pcc.hex['batman'], mec=pcc.hex['batman'], alpha=alpha)
    variable_def.fill_between(sn.lcfit.data['BessellV']['MJD'], sn.lcfit.data['BessellV']['flux_upper'], sn.lcfit.data['BessellV']['flux_lower'], color=pcc.hex['batman'], alpha=0.8, zorder=0)
    variable_def.errorbar(sn_fake.phot.data[filter_key]['MJD'], sn_fake.phot.data[filter_key]['flux'], yerr=sn_fake.phot.data[filter_key]['flux_err'], capsize=0, fmt='o', color=pcc.hex['LSST_g'], label=plot_label_string_fake, ecolor=pcc.hex['batman'], mec=pcc.hex['batman'], alpha=alpha)
xminorLocator = MultipleLocator(xminorticks)
variable_def.spines['top'].set_visible(True)
variable_def.xaxis.set_minor_locator(xminorLocator)
plot_legend = variable_def.legend(loc='upper right', scatterpoints=1, markerfirst=False, numpoints=1, frameon=False, bbox_to_anchor=(1.0, 1.0), fontsize=12.0)
variable_def.set_ylabel(yaxis_label_string)
variable_def.set_xlabel(xaxis_label_string)
print(variable_def.get_xlim())
outpath = '/Users/berto/projects/LSST/cadence/SN2007uy_consistency_check_BessellV_LSSTg'