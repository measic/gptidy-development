from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

# He3 colormap gradient
points = np.array([rad_frac_aligned*(first_line_R), dXHe3_dr]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, ax = plt.subplots()
ax.axhline(y=0.0, color='m', linestyle='--')
# Create a continuous norm to map from data points to colors | np.log10((Dthm+1).min()),np.log10((Dthm+1).max())
norm = plt.Normalize(Dthm.min(),Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
ax.set_xlabel('Radius / $R_{\odot}$')
ax.set_ylabel('d$X_{He3}$/dr / $(M_{He3}/M_{layer}) R_{\odot}$ $^{-1}$')
ax.set_xlim([0.02, 0.1])
ax.set_ylim([0, 0.1])
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = ax.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thl}$')
# add fractional radius label axis to plot
frac_x = ax.twiny()
frac_x.set_xlim(0.02/first_line_R,0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')

#plt.show()
ax.set_title('He3 abundance gradient for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_He3_radius_gradient_Dthl_color.png', bbox_inches='tight')

"""
# He3 gradient/nitrogen colormap 
points = np.array([rad_frac_aligned*(first_line_R), dXHe3_dr/XN_tp100_aligned]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, ax = plt.subplots()
ax.axhline(y=0.0, color='m', linestyle='--')
# Create a continuous norm to map from data points to colors | np.log10((Dthm+1).min()),np.log10((Dthm+1).max())
norm = plt.Normalize(Dthm.min(),Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
ax.set_xlabel('Radius / $R_{\odot}$')
ax.set_ylabel('d$X_{He3}$/dr / $(M_{He3}/M_{layer}) R_{\odot}$ $^{-1}$')
ax.set_xlim([0, 0.1])
ax.set_ylim([0, 30])
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = ax.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thermohaline}$')
# add fractional radius label axis to plot
frac_x = ax.twiny()
frac_x.set_xlim(rad_frac_aligned[0],0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')

#plt.show()
#ax.set_title('He3 abundance gradient for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
#fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_He3_radius_gradient_Dthl_color.pdf', bbox_inches='tight')

# He3 colormap abundance
points = np.array([rad_frac_aligned*(first_line_R), He3_aligned]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, ax = plt.subplots()
# Create a continuous norm to map from data points to colors
norm = plt.Normalize(Dthm.min(), Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
ax.set_xlabel('Radius / $R_{\odot}$')
ax.set_ylabel('$X_{He3}$ / $(M_{He3}/M_{layer})$')
ax.set_xlim([0, 0.1])
ax.set_ylim([0, 0.0015])
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = ax.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thermohaline}$')
# add fractional radius label axis to plot
frac_x = ax.twiny()
frac_x.set_xlim(rad_frac_aligned[0],0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')

#plt.show()
ax.set_title('He3 abundance for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_He3_abundance_Dthl_color.pdf', bbox_inches='tight')

# Helium-4 abundance colour plot
points = np.array([rad_frac_aligned*(first_line_R), He4_aligned]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
#colormap stuff
norm = plt.Normalize(Dthm.min(), Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = stam_graf0.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thermohaline}$')

stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{He4}$ / $(M_{He4}/M_{layer})$')
#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_frac_aligned[0],0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([0.25, 1])
#plt.show()
stam_graf0.set_title('He4 abundance for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_He4_abundance_Dthl_color.pdf', bbox_inches='tight')

# Helium-4 gradient plot zoomed in to show burning/thermohaline
points = np.array([rad_frac_aligned*(first_line_R), dXHe4_dr]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
#colormap stuff
norm = plt.Normalize(Dthm.min(), Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = stam_graf0.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thermohaline}$')

stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{He4}$/dr / $(M_{He4}/M_{layer}) R_{\odot}$ $^{-1}$')
#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_frac_aligned[0],0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([-0.5, 0.05])
#plt.show()
stam_graf0.set_title('He4 abundance gradient for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_He4_radius_gradient_burn_zoom_color.pdf', bbox_inches='tight')

# Nitrogen-14 abundance plot
points = np.array([rad_frac_aligned*(first_line_R), N14_aligned]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, stam_graf0 = plt.subplots()
#colormap stuff
norm = plt.Normalize(Dthm.min(), Dthm.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(Dthm)
lc.set_linewidth(2)
line = stam_graf0.add_collection(lc)
# add side color bar & label
D_color_bar = fig.colorbar(line)
D_color_bar.set_label('$D_{thermohaline}$')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{N14}$ / $(M_{N14}/M_{layer})$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x2 = stam_graf0.twiny()
frac_x2.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x2.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([0, 0.012])
#plt.show()
stam_graf0.set_title('N14 abundance for log$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_abundance_Dthl_color.pdf', bbox_inches='tight')
"""