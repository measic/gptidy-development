model_str = 'model'
with open ("mu_test_data/diff_mu_logL=2_1231_model") as model:
    print '\n    Reading physical model'
    model_data,rad_zone_model_data = data_read_CE(model,model_str)

print 'model data: ',model_data.shape, rad_zone_model_data.shape

# sort '_model' file data
mass_frac_mod = model_data[:,0]
rad_frac = model_data[:,1]
logP = model_data[:,2]
logT = model_data[:,3]
logDensity = model_data[:,4]
L_Lsurface = model_data[:,5]
eps_nuclear = model_data[:,6]
eps_grav = model_data[:,7]
eps_neutrino = model_data[:,8]
delta = model_data[:,9]
radiat = model_data[:,10]
adiab = model_data[:,11]
sound_speed = model_data[:,12]
mesh_number_mod = model_data[:,-1]


with open ("mu_test_data/diff_mu_logL=2_1231_abund") as abund:
    print '\n    Reading abundances'
    abund_data,rad_zone_abund_data = data_read_CE(abund,'abund')

# sort '_abund' file data into parameters
mass_frac_ab = abund_data[:,0]
H = abund_data[:,1]
D = abund_data[:,2]
He3 = abund_data[:,3]
He4 = abund_data[:,4]
Li7 = abund_data[:,5]
Be7 = abund_data[:,6]
C12 = abund_data[:,7]
C13 = abund_data[:,8]
N14 = abund_data[:,9]
N15 = abund_data[:,10]
O16 = abund_data[:,11]
O17 = abund_data[:,12]
O18 = abund_data[:,13]
Fe56 = abund_data[:,14]
mesh_number_ab = abund_data[:,-1]

#gradient file data

with open ("mu_test_data/diff_mu_logL=2_1231_grads") as grads:
    print '\n    Reading gradients'
    grad_data,rad_zone_grads_data = data_read_CE(grads,'grads')

mass_frac_grad = grad_data[:,0]
mu = grad_data[:,1]
dmu_dr = grad_data[:,2]
dlnmu_dr = grad_data[:,3]
del_mu = grad_data[:,4]
dXLi7_dr = grad_data[:,5]
dXC12_dr = grad_data[:,6]
dXN14_dr = grad_data[:,7]
dXHe3_dr = grad_data[:,8]
dXHe4_dr = grad_data[:,9]
# thermohaline diffusion coefficient
#Dthm = grad_data[:,10]
mesh_number_grad = grad_data[:,-1]

with open ("mu_test_data/diff_mu_logL=2_1231_eq") as eq:
    print '\n    Reading diffusion equation data'
    eq_data,rad_zone_eq_data = data_read_CE(eq,'eq')
print 'original size = ', eq_data.shape
print eq_data[-1,:]
#eq_data = eq_data[0:-1,:]
#print 'new size = ', eq_data.shape
#print eq_data[-1,:]

#Mr         R/R*         X_N          d2X_N/dr2      drho_N_rf       drho_N_rb        dr
#d2rho_N/dr     d2rho_N/dr2    rho_N(t)       rho_N(t+dt)   rho_N(t+dt)_var   MESH

mass_frac_eq = eq_data[:,0]
rfrac_eq = eq_data[:,1]
Dthm = eq_data[:,2]
br_prod_minus = eq_data[:,3]
br_prod_minus_var = eq_data[:,4]
br_prod_plus = eq_data[:,5]
br_prod_plus_var = eq_data[:,6]
X_N_t = eq_data[:,7]
X_N_tpdt = eq_data[:,8]
X_N_tpdt_var = eq_data[:,9]
mesh_number_eq = eq_data[:,-1]

if (len(logDensity) == 1424 and len(eq_data[:,0]) == 1424):
    logDensity_red = logDensity[0:-1]
    eq_data_red = eq_data[0:-1,:]

    mass_frac_eq = eq_data_red[:,0]
    rfrac_eq = eq_data_red[:,1]
    Dthm = eq_data_red[:,2]
    br_prod_minus = eq_data_red[:,3]
    br_prod_minus_var = eq_data_red[:,4]
    br_prod_plus = eq_data_red[:,5]
    br_prod_plus_var = eq_data_red[:,6]
    XN_t_eq = eq_data_red[:,7]
    XN_tpdt_eq = eq_data_red[:,8]
    XN_tpdt_var_eq = eq_data_red[:,9]
    mesh_number_eq = eq_data_red[:,-1]

with open ("mu_test_data/diff_mu_logL=2_1231_time_Dvar_test") as time:
    print '\n    Reading diffusion equation time-step results'
    time_data,rad_zone_time_data = data_read_CE(time,'time')
    
mass_frac_tm = time_data[:,0]
XN_t = time_data[:,1]
XN_tp1 = time_data[:,2]
XN_tp10 = time_data[:,3]
XN_tp20 = time_data[:,4]
XN_tp30 = time_data[:,5]
XN_tp40 = time_data[:,6]
XN_tp50 = time_data[:,7]
XN_tp60 = time_data[:,8]
XN_tp70 = time_data[:,9]
XN_tp80 = time_data[:,10]
XN_tp90 = time_data[:,11]
XN_tp100 = time_data[:,12]
mesh_number_tm = time_data[:,-1]

print model_data.shape
print abund_data.shape
print grad_data.shape
print eq_data.shape
print time_data.shape

nuc_burn_model_data = data_focus(eps_nuclear,1, model_data)
nuc_burn_abund_data = focus_sync(nuc_burn_model_data, abund_data)
nuc_burn_grads_data = focus_sync(nuc_burn_model_data, grad_data)

first_line_R = 2.21E+01
# define quantities for the nuclear burning region
# same quantities, but arrays are restricted to regions covered by 'nuc_burn_' arrays
nuc_rad_frac = nuc_burn_model_data[:,1]
nuc_logP = nuc_burn_model_data[:,2]
nuc_mesh_number_mod = nuc_burn_model_data[:,-1]

nuc_Li7 = nuc_burn_abund_data[:,5]
nuc_C12 = nuc_burn_abund_data[:,7]
nuc_N14 = nuc_burn_abund_data[:,9]

#nuc_mol_mass = nuc_burn_abund_data[:,15]
#lnmu_nuc = np.log(nuc_mol_mass)
#logmu_nuc = np.log10(nuc_mol_mass)
#nuc_lnmu_lnp = nuc_burn_abund_data[:,18]
#nuc_dXLi7_dr = nuc_burn_abund_data[:,19]
#nuc_dXC12_dr = nuc_burn_abund_data[:,20]
#nuc_dXN14_dr = nuc_burn_abund_data[:,21]
nuc_mesh_number_ab = nuc_burn_abund_data[:,-1]

model_data_aligned = focus_sync(grad_data,model_data)
abund_data_aligned = focus_sync(grad_data,abund_data)
time_data_aligned = focus_sync(grad_data,time_data)

rad_frac_aligned = model_data_aligned[:,1]
logDens_aligned = model_data_aligned[:,4]
He4_aligned = abund_data_aligned[:,4]
He3_aligned = abund_data_aligned[:,3]
N14_aligned = abund_data_aligned[:,9]

XN_tp100_aligned = time_data_aligned[:,12]