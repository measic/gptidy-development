# diffusion equation plot
n_lines = 12

fig, stam_graf0 = plt.subplots()
#stam_graf0.plot(nuc_burn_model_data[:,2], nuc_mol_mass, 'r')
stam_graf0.axhline(y=0.0, color='k', linestyle='--', label = '$X_{N14}(r,t) = 0$')

# colormap stuff
col_map = plt.cm.gnuplot
plt.gca().set_color_cycle([col_map(i) for i in np.linspace(0, 0.9, n_lines)])


stam_graf0.plot(rfrac_eq*(first_line_R), XN_t, label ='$t=t_{0}$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp1, label ='$t=t_{0}+\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp10, label ='$t=t_{0}+10\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp20, label ='$t=t_{0}+20\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp30, label ='$t=t_{0}+30\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp40, label ='$t=t_{0}+40\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp50, label ='$t=t_{0}+50\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp60, label ='$t=t_{0}+60\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp70, label ='$t=t_{0}+70\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp80, label ='$t=t_{0}+80\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp90, label ='$t=t_{0}+90\\delta t$')
stam_graf0.plot(rfrac_eq*(first_line_R), XN_tp100, label ='$t=t_{0}+100\\delta t$')

xind = np.argmax(XN_tp100)
print xind
print del_mu.shape,dXHe4_dr.shape,rfrac_eq.shape

stam_graf0.set_xlabel('Radius / $R_{\odot}$')
stam_graf0.set_ylabel('$X_{N14}(r,t)$ / $(M_{N14}/M_{layer})$')
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1.1))

#print max(drho_N_dt),min(drho_N_dt)
#print rfrac_eq[0],rfrac_eq[-1]

#add fractional radius label to plot
frac_x = stam_graf0.twiny()
frac_x.set_xlim((0.02/first_line_R),(0.1/first_line_R))
frac_x.set_xlabel('Fractional radius')
stam_graf0.set_ylim([-0.001, 0.055])
stam_graf0.set_xlim([0.02, 0.1])
plt.show() #\n1M_sun, Z=Z_sun with diffusion' $D=1.457 \\times 10^{6}$ variable $D$
stam_graf0.set_title('$X_{N14}(r,t)$ for thermohaline diffusion equation with \n variable $D$ and $\\delta t=500$yr for log$(L/L_{\odot})$ = 2.1231,\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_time_diff_eq_Dvar_10dt_dmu_k_lim.png', bbox_inches='tight')

print del_mu[361]

fig, stam_graf1 = plt.subplots()
stam_graf1.axhline(y=0.0, color='k', linestyle='--')
stam_graf1.axhline(y=del_mu[361], color='m', linestyle='--')
stam_graf1.plot(rad_frac_aligned*(first_line_R), del_mu, color='b', label =r'$\nabla_{\mu}$')
#stam_graf1.plot(rad_frac_aligned*(first_line_R), dXHe4_dr, color='g', label ='$dX_{He4}/dr$')

stam_graf1.set_xlabel('Radius / $R_{\odot}$')
stam_graf1.set_ylabel('Gradient')
#plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1.1))
#add fractional radius label to plot
frac_x = stam_graf1.twiny()
frac_x.set_xlim((0.02/first_line_R),(0.03/first_line_R))
frac_x.set_xlabel('Fractional radius')
stam_graf1.set_ylim([-0.001, 0.001])
stam_graf1.set_xlim([0.02, 0.03])
plt.show() #\n1M_sun, Z=Z_sun with diffusion' $D=1.457 \\times 10^{6}$ variable $D$
stam_graf1.set_title('$\\nabla _{\mu}$,$dX_{He4}/dr$ vs radius for log$(L/L_{\odot})$ = 2.1231,\n 1$M_{\odot}$, $Z=Z_{\odot}$ with diffusion', y=1.15)
#fig.savefig('mu_test_data/mu_test_graphs/eq_logL=2.1231_time_diff_eq_Dvar_mu_inv.pdf', bbox_inches='tight')
