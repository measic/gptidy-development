K_therm_21 = (D_21*rad_ad_21)/(1000*del_mu_21)
K_therm_25 = (D_25*rad_ad_25)/(1000*del_mu_25)
K_therm_27 = (D_27*rad_ad_27)/(1000*del_mu_27)

del_ratio_21 = del_mu_21/rad_ad_21
del_ratio_25 = del_mu_25/rad_ad_25
del_ratio_27 = del_mu_27/rad_ad_27

logP_degen_21 = model_degen_21[:,2]
logP_degen_25 = model_degen_25[:,2]
logP_degen_27 = model_degen_27[:,2]

logDens_degen_21 = model_degen_21[:,4]
logDens_degen_25 = model_degen_25[:,4]
logDens_degen_27 = model_degen_27[:,4]

test_grad = (3.0e9)/(-3.0e10)

# for P = k*(rho^(5/3)):
# logP = (5/3)*log(rho) + log(k)
#-> log(k) = (logP_0)-((5/3)*log(rho_0))
av_logP_degen_C = (logP_degen_21[0] + logP_degen_25[0] + logP_degen_27[0])/(3.0)
av_logDens_degen_C = (logDens_degen_21[0] + logDens_degen_25[0] + logDens_degen_27[0])/(3.0)
av_logP_degen_edge = (logP_degen_21[-1] + logP_degen_25[-1] + logP_degen_27[-1])/(3.0)
av_logDens_degen_edge = (logDens_degen_21[-1] + logDens_degen_25[-1] + logDens_degen_27[-1])/(3.0)
dens_P_intercept = av_logP_degen_C-((5.0/3.0)*av_logDens_degen_C)

#dens_P_intercept_edge = logP_degen_21[-1]-((5/3)*logDens_degen_21[-1])
central_grad_21 = (logP_degen_21[0] - logP_degen_21[10])/(logDens_degen_21[0] - logDens_degen_21[10])
degen_edge_grad_21 = (logP_degen_21[-11] - logP_degen_21[-1])/(logDens_degen_21[-11] - logDens_degen_21[-1])
boundary_intercept = av_logP_degen_edge-(degen_edge_grad_21*av_logDens_degen_edge)
central_intercept = av_logP_degen_C-(central_grad_21*av_logDens_degen_C)
print central_grad_21, degen_edge_grad_21,(5.0/3.0)

fig, stam_graf0 = plt.subplots()
stam_graf0.axvline(x=K_therm_27[np.argmax(D_27)], color='m', linestyle='--',label='log$(L/L_{\odot})$=2.1231 max')
stam_graf0.plot(K_therm_21, D_21,'r', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.plot(K_therm_25, D_25,'g', label='log$(L/L_{\odot})$=2.5001')
stam_graf0.plot(K_therm_27, D_27, 'b', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.set_xlabel('Thermal diffusivity / cm$^{2}$s$^{-1}$')
stam_graf0.set_ylabel('$D_{therm}$ / cm$^{2}$s$^{-1}$')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 0.7))
stam_graf0.set_xlim(0,1e10)
stam_graf0.set_title('Thermohaline coefficients vs thermal diffusivity\n for various log$(L/L_{\odot})$ for 1M_sun, Z=Z_sun\n with diffusion', y=1.05)
plt.show()
fig.savefig('mu_test_data/mu_test_graphs/logL=various_therm_diff_Dtherm.pdf', bbox_inches='tight')

fig, stam_graf0 = plt.subplots()
stam_graf0.axvline(x=del_ratio_27[np.argmax(D_27)], color='m', linestyle='--',label='log$(L/L_{\odot})$=2.1231 max')
stam_graf0.plot(del_ratio_21, D_21,'r', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.plot(del_ratio_25, D_25,'g', label='log$(L/L_{\odot})$=2.5001')
stam_graf0.plot(del_ratio_27, D_27, 'b', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.set_xlabel(r'$\nabla_{\mu}/(\nabla_{rad} - \nabla_{ad})$')
stam_graf0.set_ylabel('$D_{therm}$ / cm$^{2}$s$^{-1}$')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 0.7))
stam_graf0.set_xlim(-0.0005,0.002)
stam_graf0.set_title('Thermohaline coefficients vs nabla ratio\n for various log$(L/L_{\odot})$ for 1M_sun, Z=Z_sun\n with diffusion', y=1.05)
plt.show()
fig.savefig('mu_test_data/mu_test_graphs/logL=various_nabla_ratio_Dtherm.pdf', bbox_inches='tight')

fig, stam_graf0 = plt.subplots() #central_grad_21, degen_edge_grad_21
stam_graf0.plot(logDens_degen_21,(logDens_degen_21*central_grad_21 + central_intercept),color='c', linestyle='--',label='central gradient = 1.5443')
stam_graf0.plot(logDens_degen_21,(logDens_degen_21*degen_edge_grad_21 + boundary_intercept),color='k', linestyle='--',label='boundary gradient = 0.9900')
stam_graf0.plot(logDens_degen_21,(logDens_degen_21*(5.0/3.0) + dens_P_intercept),color='m', linestyle='--',label='CC gradient = 5/3')
stam_graf0.plot(logDens_degen_21, logP_degen_21,'r', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.plot(logDens_degen_25, logP_degen_25,'g', label='log$(L/L_{\odot})$=2.5001')
stam_graf0.plot(logDens_degen_27, logP_degen_27, 'b', label='log$(L/L_{\odot})$=2.1231')
stam_graf0.set_xlabel(r'log($\rho$)')
stam_graf0.set_ylabel('log(P)')
plt.legend(loc='upper left', bbox_to_anchor=(1.0, 0.7))
#stam_graf0.set_xlim(-0.0005,0.002)
stam_graf0.set_title('He-core pressure-density plot for various\n log$(L/L_{\odot})$ for 1M_sun, Z=Z_sun with diffusion', y=1.05)
plt.show()
fig.savefig('mu_test_data/mu_test_graphs/logL=various_core logP_logDens.pdf', bbox_inches='tight')