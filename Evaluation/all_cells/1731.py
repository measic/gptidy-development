# Create a figure
sns.set_style("ticks")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')


plotError = True

ax1.plot(elder_area_value, elder_area_density, lw=1, color='r', label="Elder");
ax1.plot(fox_area_value, fox_area_density, linestyle = '--', lw=1, color='r', label="Fox");
# ax1.plot(round1_area_density, round1_area_value, lw=1, color='orange');
# ax1.plot(round2_area_density, round2_area_value, lw=1, color='teal');

ax1.plot(hank_area_value, hank_area_density, lw=1, color='b', label="Hank");
ax1.plot(dry_area_value, dry_area_density, linestyle = '--', lw=1, color='b', label="Dry");
ax1.legend(bbox_to_anchor=(.9, .5))

ax1.axes.get_yaxis().set_visible(False)
ax1.axes.get_xaxis().set_visible(False)
ax1.set_xscale('log')
ax1.set_frame_on(False)

symbolSize = 30
ax3.scatter(.5*(area_bins_elder[1:]+area_bins_elder[:-1]),bin_medians_elder, s=symbolSize, marker = "o", color = 'r', label="Elder")
ax3.scatter(.5*(area_bins_fox[1:]+area_bins_fox[:-1]),bin_medians_fox, s=symbolSize, marker = "s", color = 'r', label="Fox")
ax3.scatter(.5*(area_bins_hank[1:]+area_bins_hank[:-1]),bin_medians_hank, s=symbolSize, marker = "o", color = 'b', label="Hank")
ax3.scatter(.5*(area_bins_dry[1:]+area_bins_dry[:-1]),bin_medians_dry, s=symbolSize, marker = "s", color = 'b', label="Dry")

if plotError:
    ax3.errorbar(.5*(area_bins_elder[1:]+area_bins_elder[:-1]),bin_medians_elder, yerr=bin_stds_elder, fmt = None, capthick=0, ecolor = 'r')
    ax3.errorbar(.5*(area_bins_fox[1:]+area_bins_fox[:-1]),bin_medians_fox, yerr=bin_stds_fox, fmt = None, capthick=0, ecolor = 'r')
    ax3.errorbar(.5*(area_bins_hank[1:]+area_bins_hank[:-1]),bin_medians_hank, yerr=bin_stds_hank, fmt = None, capthick=0, ecolor = 'b')
    ax3.errorbar(.5*(area_bins_dry[1:]+area_bins_dry[:-1]),bin_medians_dry, yerr=bin_stds_dry, fmt = None, capthick=0, ecolor = 'b')

#ax3.fill_between(.5*(area_bins_elder[1:]+area_bins_elder[:-1]),np.subtract(bin_medians_elder, bin_stds_elder), np.add(bin_medians_elder,bin_stds_elder), color = 'r', alpha=0.3)
#ax3.fill_between(.5*(area_bins_fox[1:]+area_bins_fox[:-1]),np.subtract(bin_medians_fox, bin_stds_fox), np.add(bin_medians_fox,bin_stds_fox), color = 'k', alpha=0.3)
#ax3.fill_between(.5*(area_bins_hank[1:]+area_bins_hank[:-1]),np.subtract(bin_medians_hank, bin_stds_hank), np.add(bin_medians_hank,bin_stds_hank), color = 'b', alpha=0.3)
#ax3.fill_between(.5*(area_bins_dry[1:]+area_bins_dry[:-1]),np.subtract(bin_medians_dry, bin_stds_dry), np.add(bin_medians_dry,bin_stds_dry), color = 'y', alpha=0.3)


symbolSize = 10
alphaLevel=1
# ax3.scatter(r1['flowacc_co'], r1['slp_deg_co'], zorder=100,
#             alpha=alphaLevel, marker = "s", color='orange',
#             label = 'Round 1', s=symbolSize)
# ax3.scatter(r2['flowacc_co'], r2['slp_deg_co'], zorder=100,
#             alpha=alphaLevel, marker = "o", color='teal',
#             label = 'Round 2', s=symbolSize)


ax3.legend(bbox_to_anchor=(.95, .95))
ax3.set_ylabel("Hillslope angle [  $^{\circ}$ ]")
ax3.set_xlabel("Upslope contributing area [ m$^2$]")
ax3.set_ylim([0,60])
ax3.set_xlim([1,10000000])
# ax3.set_yscale('log')
ax3.set_xscale('log')


ax4.plot(elder_slope_density, elder_slope_value, lw=1, color='r');
ax4.plot(fox_slope_density, fox_slope_value, linestyle = '--', lw=1, color='r');
ax4.plot(hank_slope_density, hank_slope_value, lw=1, color='b');
ax4.plot(dry_slope_density, dry_slope_value, linestyle = '--', lw=1, color='b');
# ax4.set_yscale('log')
# ax4.plot(round1_slope_density, round1_slope_value, lw=1, color='orange');
# ax4.plot(round2_slope_density, round1_slope_value, lw=1, color='teal');

ax4.axes.get_yaxis().set_visible(False)
ax4.axes.get_xaxis().set_visible(False)



sns.despine()



fig.subplots_adjust(hspace=0)
fig.subplots_adjust(wspace=0)

ax2.axis('off')
fig.set_size_inches(10, 10)
fig.savefig('logS_vs_logA_a_Daniella.pdf', transparent=True, pad_inches=0)

plt.show()
