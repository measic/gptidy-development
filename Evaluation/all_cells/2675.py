"""# diffusion equation plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rfrac_eq*(first_line_R), drho_N_dt, 'r')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel(r'$d\rho_{N14}/dt$ / gcm$^{-3}$s$^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.55, 1.0))

print max(drho_N_dt),min(drho_N_dt)
print rfrac_eq[0],rfrac_eq[-1]

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_ylim([-3e-8, 3e-8])
stam_graf0.set_xlim([0, 0.1])
#plt.show() \n1M_sun, Z=Z_sun with diffusion'
stam_graf0.set_title('drho(N14)/dt for thermohaline diffusion equation with \nD=(1.457x10^6) for log$(L/L_{\odot})$ = 2.1231', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_drho_dt_radius.pdf', bbox_inches='tight')
"""

# Nitrogen-14 gradient plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rad_frac_aligned*(first_line_R), dXN14_dr, 'g')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{N14}$/dr / $(M_{N14}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x1 = stam_graf0.twiny()
frac_x1.set_xlim(min(rad_frac_aligned),(0.1/first_line_R))
frac_x1.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
#stam_graf0.set_ylim([-0.0003, 0.001])
#plt.show()
stam_graf0.set_title('N14 abundance gradient for log$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_radius_gradient.pdf', bbox_inches='tight')

# Nitrogen-14 second derivative plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rfrac_eq*(first_line_R), d2N14_dr2, 'c')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$^{2}X_{N14}$/dr$^{2}$ / $(M_{N14}/M_{layer}) R_{\odot}$ $^{-2}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x3 = stam_graf0.twiny()
frac_x3.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x3.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([-2e-18, 7e-18])
#plt.show()
stam_graf0.set_title('N14 abundance second differential for log$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_radius_2xdiff.pdf', bbox_inches='tight')

# Nitrogen-14 abundance/mass density ratio plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.plot(rfrac_eq*(first_line_R), (d2N14_dr2/d2rho_N_dr2), 'k')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{N14}$"/$\\rho$" ratio')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x3 = stam_graf0.twiny()
frac_x3.set_xlim(min(rfrac_eq),(0.1/first_line_R))
frac_x3.set_xlabel('Fractional radius')
stam_graf0.set_xlim([0, 0.1])
stam_graf0.set_ylim([-5.5, 1])
#plt.show()
stam_graf0.set_title('N14 abundance/density second\n differential ratio for log$(L/L_{\odot})$ = 2.1231\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_N14_density_2xdiff_ratio.pdf', bbox_inches='tight')