# Lithium-7 plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,5], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{Li7}$/dr / $(M_{Li7}/M_{layer}) R_{\odot}$ $^{-1}$')# d$X_{Li7}$/dr R_{\odot}$ $^{-1}
#plt.legend(loc='upper left', bbox_to_anchor=(0.55, 1.0))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')
#stam_graf0.set_ylim([-0.0003, 0.001])
#plt.show()
stam_graf0.set_title('Li7 abundance gradient for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_Li7_radius_gradient_19.pdf', bbox_inches='tight')



# Carbon-12 plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,6], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{C12}$/dr / $(M_{C12}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.6))
# nuc_dXLi7_dr_correction/rad_fraction_to_Rsun

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_xlim([0.03, 0.001])
#plt.show()
stam_graf0.set_title('C12 abundance gradient for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_C12_radius_gradient_19.pdf', bbox_inches='tight')

# Nitrogen-14 plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
# nuc_dXLi7_dr_correction/rad_fraction_to_Rsun
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,7], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{N14}$/dr / $(M_{N14}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-0.0003, 0.001])
#plt.show()
stam_graf0.set_title('N14 abundance gradient for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_N14_radius_gradient_19.pdf', bbox_inches='tight')

# Helium-3 plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
# nuc_dXLi7_dr_correction/rad_fraction_to_Rsun
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,8], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{He3}$/dr / $(M_{He3}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-0.0003, 0.001])
#plt.show()
stam_graf0.set_title('He3 abundance gradient for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_He3_radius_gradient_19.pdf', bbox_inches='tight')

# Helium-4 plot
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='m', linestyle='--') #,label='no change in abundance'
# nuc_dXLi7_dr_correction/rad_fraction_to_Rsun
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,9], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{He4}$/dr / $(M_{He4}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-0.0003, 0.001])
#plt.show()
stam_graf0.set_title('He4 abundance gradient for burning region for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_He4_radius_gradient_19.pdf', bbox_inches='tight')

# molecular weight
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(logP[:-1], mol_mass, 'r')
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,2], 'c')
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$\mu$/dr / $(M_{i}/M_{layer}) R_{\odot}$ $^{-1}$')

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_title('Molecular weight gradient for \nburning region for log$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_mu_grad.pdf', bbox_inches='tight')

# diffusion coefficients
fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(logP[:-1], mol_mass, 'r')
stam_graf0.plot(nuc_rad_frac*(first_line_R), nuc_burn_grads_data[:,10], 'k')
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('D$_{therm}$ / cm$^{2}$s$^{-1}$')
#stam_graf0.set_ylim(min(nuc_burn_grads_data[:,10])-100000,max(nuc_burn_grads_data[:,10])+100000)

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(nuc_rad_frac[0],nuc_rad_frac[-1])
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_title('Thermohaline diffusion coefficent \nplot for log$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/burning_logL=2.1231_coefficients_if.pdf', bbox_inches='tight')
print 'minimum value of Dthm = ',min(nuc_burn_grads_data[:,10])
