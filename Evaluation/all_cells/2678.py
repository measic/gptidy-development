# Radiation zone plots

rad_zone_abund_data = focus_sync(rad_zone_model_data, abund_data)
rad_zone_grads_data = focus_sync(rad_zone_model_data, grad_data)
print rad_zone_abund_data.shape
print rad_zone_grads_data.shape
print bound_inds
print nuc_burn_model_data[-1,1]

with open ("mu_test_data/2_1231_rad_stuff","w") as f:
    for i in range(len(rad_zone_model_data[:,0])): 
        rad_zone_model_data[i,1].tofile(f," "),f.write(' '),rad_zone_grads_data[i,6].tofile(f," "),f.write(' '),rad_zone_grads_data[i,7].tofile(f," "),f.write(' '),rad_zone_grads_data[i,4].tofile(f," ")
        f.write('\n')

# Carbon-12 plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.axvline(x=(first_line_R*nuc_burn_model_data[-1,1]), color='c', linestyle='--')
stam_graf0.plot(rad_zone_model_data[:,1]*(first_line_R), rad_zone_grads_data[:,6], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{C12}$/dr / $(M_{C12}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.6))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_zone_model_data[0,1],rad_zone_model_data[-1,1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-1e-06, 1e-06])_focus
#plt.show()
stam_graf0.set_title('C12 abundance gradient for radiative zone for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/rad_logL=2.1231_C12_radius_gradient.pdf', bbox_inches='tight')

# Nitrogen-14 plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.axvline(x=(first_line_R*nuc_burn_model_data[-1,1]), color='c', linestyle='--')
stam_graf0.plot(rad_zone_model_data[:,1]*(first_line_R),rad_zone_grads_data[:,7], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('d$X_{N14}$/dr / $(M_{N14}/M_{layer}) R_{\odot}$ $^{-1}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_zone_model_data[0,1],rad_zone_model_data[-1,1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-1e-06, 1e-06])_focus
#plt.show()
stam_graf0.set_title('N14 abundance gradient for radiative zone for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/rad_logL=2.1231_N14_radius_gradient.pdf', bbox_inches='tight')

"""
# dln(mu)/dln(P) plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.axvline(x=(first_line_R*nuc_burn_model_data[-1,1]), color='c', linestyle='--')
stam_graf0.plot(rad_zone_model_data[:,1]*(first_line_R), rad_zone_grads_data[:,4], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel(r'$\nabla_{\mu}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_zone_model_data[0,1],rad_zone_model_data[-1,1])
frac_x.set_xlabel('Fractional radius')

stam_graf0.set_ylim([-1e-06, 1e-06])
#plt.show()
stam_graf0.set_title('dln(mu)/dln(P) for radiative zone for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/rad_logL=2.1231_nabla_mu_focus.pdf', bbox_inches='tight')

# dln(mu)/dln(P) plot
fig, stam_graf0 = plt.subplots()
stam_graf0.axhline(y=0.0, color='m', linestyle='--')
stam_graf0.axvline(x=(first_line_R*nuc_burn_model_data[-1,1]), color='c', linestyle='--')
stam_graf0.plot(rad_zone_model_data[:,1]*(first_line_R), rad_zone_grads_data[:,4], 'r')#, label='(k-1) to (k+1)'
stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel(r'$\nabla_{\mu}$')
#plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim(rad_zone_model_data[0,1],rad_zone_model_data[-1,1])
frac_x.set_xlabel('Fractional radius')

#stam_graf0.set_ylim([-1e-04, 1e-04])
#plt.show()
stam_graf0.set_title('dln(mu)/dln(P) for radiative zone for \nlog$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/rad_logL=2.1231_nabla_mu.pdf', bbox_inches='tight')
"""