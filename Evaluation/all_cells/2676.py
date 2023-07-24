# time-change plots

# Nitrogen-14 small-time change plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rfrac_eq*(first_line_R), (rho_N_tpdt - rho_N_t), 'b', label='fixed D = 1.457x10$^{6}$')
stam_graf0.plot(rfrac_eq*(first_line_R), (rho_N_tpdt_var - rho_N_t)-15, 'r',label='$\\mu$-constrained D,\n zeroed at -15')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel(r'$\rho_{N14}(t+dt) - \rho_{N14}(t)$')
plt.legend(loc='upper left', bbox_to_anchor=(0.45, 0.95))

#add fractional radius label to plot
frac_x3 = stam_graf0.twiny()
frac_x3.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x3.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([-20, 15])
#plt.show()
stam_graf0.set_title('N14 density time change for log$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_density_time_change.pdf', bbox_inches='tight')


# Nitrogen-14 small-time change plot - mass fractions
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rfrac_eq*(first_line_R), (rho_N_tpdt - rho_N_t)/(10**logDensity_red), 'g')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{N}(t+dt) - X_{N}(t)$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x3 = stam_graf0.twiny()
frac_x3.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x3.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
#stam_graf0.set_ylim([-0.0005, 0.0005])
#plt.show()
stam_graf0.set_title('N14 mass-fraction time (fixed D) change for \nlog$(L/L_{\odot})$ = 2.1231 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_mass_frac_time_change.pdf', bbox_inches='tight')


# Density plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.axhline(y=0.0, color='m', linestyle='--')
# nuc_dXLi7_dr_correction/rad_fraction_to_Rsun
stam_graf0.plot(rad_frac*(first_line_R), logDensity, 'r')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('Density')

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_frac[0],0.1/first_line_R)
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
#stam_graf0.set_ylim([-0.002, 0.002])
#plt.show()
stam_graf0.set_title('Density-radius plot for \nlog$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_density_radius.pdf', bbox_inches='tight')