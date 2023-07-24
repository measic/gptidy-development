# Multiple species and diffsuion coefficient plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
# scale curve data such that they fit onto the same axes while remaining visible
scale_factor_D = abs(max(nuc_burn_grads_data[:,10])/max(nuc_burn_grads_data[:,8]))
scale_factor_C = abs(max(nuc_burn_grads_data[:,6])/max(nuc_burn_grads_data[:,8]))
scale_factor_N = abs(min(nuc_burn_grads_data[:,7])/max(nuc_burn_grads_data[:,8]))
scale_factor_Li = abs(max(nuc_burn_grads_data[:,5])/max(nuc_burn_grads_data[:,8]))#x 10$^{11}$
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,8],'r', label='d$X_{He3}$/dr')# He3
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,5]/scale_factor_Li,'c', label='d$X_{Li7}$/dr')# Li7 
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,10]/scale_factor_D, 'k', label='D$_{therm}$')# Dthm
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,7]/scale_factor_N, 'b', label='d$X_{N14}$/dr')
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,6]/scale_factor_C, 'g', label='d$X_{C12}$/dr')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{He3}$/dr / $(M_{He3}/M_{layer}) R_{\odot}$ $^{-1}$')# d$X_{Li7}$/dr R_{\odot}$ $^{-1}
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 0.7))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
#d_therm = stam_graf0.twinx()
#d_therm.set_ylim(min(nuc_burn_grads_data[:,10])-100000,max(nuc_burn_grads_data[:,10])+100000)
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')
#d_therm.set_ylabel('D(thermohaline)')
stam_graf0.set_title('Abundance gradients for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)

plt.show()
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_species_radius_gradient_Dtherm_if.pdf', bbox_inches='tight')

fig, stam_graf0 = plt.subplots()
# scale curve data such that they fit onto the same axes while remaining visible
scale_factor_He3 = abs(max(nuc_burn_abund_data[:,3]))
scale_factor_D = abs(max(nuc_burn_grads_data[:,10]))#/max(nuc_burn_abund_data[:,3]))
scale_factor_C = abs(max(nuc_burn_abund_data[:,7]))#/max(nuc_burn_abund_data[:,3]))
scale_factor_N = abs(max(nuc_burn_abund_data[:,9]))#/max(nuc_burn_abund_data[:,3]))
scale_factor_Li = abs(max(nuc_burn_abund_data[:,5]))#/max(nuc_burn_abund_data[:,3]))#x 10$^{11}$
scale_factor_O = abs(max(nuc_burn_abund_data[:,11]))#/max(nuc_burn_abund_data[:,3]))#x 10$^{11}$
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_abund_data[:,3]/scale_factor_He3,'r', label='He3')# He3
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_abund_data[:,5]/scale_factor_Li,'c', label='Li7')# Li7 
#stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,10]/scale_factor_D, 'k', label='D$_{therm}$')# Dthm
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_abund_data[:,9]/scale_factor_N, 'b', label='N14')
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_abund_data[:,7]/scale_factor_C, 'g', label='C12')
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_abund_data[:,11]/scale_factor_O, 'y', label='O16')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{i}$ / $M_{i}/M_{layer}$')# d$X_{Li7}$/dr R_{\odot}$ $^{-1}
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 0.7))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
#d_therm = stam_graf0.twinx()
#d_therm.set_ylim(min(nuc_burn_grads_data[:,10])-100000,max(nuc_burn_grads_data[:,10])+100000)
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')
#d_therm.set_ylabel('D(thermohaline)')
stam_graf0.set_title('Abundance gradients for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)

plt.show()
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2p1231_5species.pdf', bbox_inches='tight')#_Dtherm_if

"""
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(logP[:-1], mol_mass, 'r')
stam_graf0.plot(logP, logT, 'k')
stam_graf0.set_xlabel('log(P)')
stam_graf0.set_ylabel('log(T$_{eff}$)')
stam_graf0.set_title('temperature-pressure plot for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion')
fig.savefig('mu_test_data/mu_test_graphs/logL=2.1231_logT_logP.pdf', bbox_inches='tight')
"""