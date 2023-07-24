#nuc_dXLi7_dr_correction = nuc_burn_abund_data[:,19]*6.9599
#nuc_dXC12_dr_correction = nuc_burn_abund_data[:,20]*6.9599
#nuc_dXN14_dr_correction = nuc_burn_abund_data[:,21]*6.9599
# radius in solar units = R/Ro in stampe (_header) file format = log of 'R' in 1st line

#rad_fraction_to_Rsun = (10**first_line_R)
#rad_fraction_to_metres = (10**first_line_R)*(6.957*(10**8))

# check cell continuity
#print y_param_names[0]

#print abund_data[-1,:]
#print model_data[-1,:]
#data_list=[]
#data_list_2=[]

print eps_nuclear #[i]
print nuc_burn_model_data.shape
print nuc_burn_abund_data.shape
print ((1 + nuc_mesh_number_mod[-1]) - nuc_mesh_number_mod[0])
print ((1 + nuc_mesh_number_ab[-1]) - nuc_mesh_number_ab[0])
#print nuc_burn_model_data[:,-1]
#print nuc_burn_abund_data[:,-1]
print 'diff loop start'
# check that both arrays cover the same layers of the star
for i in range(len(nuc_burn_model_data[:,-1])):
    diff = nuc_burn_model_data[i,-1] - nuc_burn_abund_data[i,-1]
    if diff != 0:
        print diff
print 'diff loop complete'

print first_line_R

nuc_data_list=[]
nuc_data_list_2=[]
#nuc_grad_list_2=[]
nuc_data_list_3=[]
"""
for i in range(1,len(Li7)-1):
    line_list = []
    j = i+1
    #print j
    dXLi7 = Li7[j] - Li7[i]
    dXC12 = C12[j] - C12[i]
    dXN14 = N14[j] - N14[i]
    drad = (rad_frac[j] - rad_frac[i])*22.1
    #print drad, mesh_number_ab[i]
    line_list = [dXLi7/drad, dXC12/drad, dXN14/drad, mesh_number_ab[i]]
    #data_list.append(line_list)
    if (mesh_number_ab[i] in nuc_burn_abund_data[:,-1]):
        nuc_data_list.append(line_list)
        #print mesh_number_ab[i]

for i in range(1,len(Li7)-1):
    line_list_2 = []
    h = i-1
    j = i+1
    #print j
    dXLi7 = Li7[j] - Li7[h]
    dXC12 = C12[j] - C12[h]
    dXN14 = N14[j] - N14[h]
    drad = (rad_frac[j] - rad_frac[h])*22.1
    check_rad = (rad_frac[j] - rad_frac[i])*22.1
    #print drad, check_rad, mesh_number_ab[i]
    line_list_2 = [dXLi7/drad, dXC12/drad, dXN14/drad, mesh_number_ab[i]]
    #grad_list_2 = [dXLi7_dr_stam[i], dXC12_dr_stam[i], dXN14_dr_stam[i], mesh_number_grad[i]]
    #print Li7[i],dXLi7,drad,dXLi7/drad,dXLi7_dr_stam[i-1]
    #data_list_2.append(line_list) and mesh_number_grad[i] in nuc_burn_abund_data[:,-1]
    if (mesh_number_ab[i] in nuc_burn_abund_data[:,-1] ):
        nuc_data_list_2.append(line_list_2)
        #nuc_grad_list_2.append(grad_list_2)
        #print mesh_number_ab[i], mesh_number_mod[i]

for i in range(1,len(Li7)-1):
    line_list_3 = []
    h = i-1
    #print j
    dXLi7 = Li7[i] - Li7[h]
    dXC12 = C12[i] - C12[h]
    dXN14 = N14[i] - N14[h]
    drad = (rad_frac[i] - rad_frac[h])*22.1
    #check_rad = (rad_frac[j] - rad_frac[i])*22.1
    #print drad, check_rad, mesh_number_ab[i]
    line_list_3 = [dXLi7/drad, dXC12/drad, dXN14/drad, mesh_number_ab[i]]
    #data_list_2.append(line_list)
    if (mesh_number_ab[i] in nuc_burn_abund_data[:,-1]):
        nuc_data_list_3.append(line_list_3)
        #print mesh_number_ab[i], mesh_number_mod[i]
        
     
nuc_stampe_data_arr = np.array(nuc_data_list)
nuc_stampe_data_arr_2 = np.array(nuc_data_list_2)
#nuc_stampe_grad_arr_2 = np.array(nuc_grad_list_2)
nuc_stampe_data_arr_3 = np.array(nuc_data_list_3)
# data_arr_2 = np.array(data_list_2)
#dXLi7_dr = dXLi7_dr[:-1]
print nuc_stampe_data_arr_2.shape"""
print dXLi7_dr.shape
print nuc_rad_frac.shape
#print 

#for i in range(1,len(nuc_stampe_data_arr[:,-1])):
#    print nuc_stampe_data_arr[i,0]/nuc_stampe_data_arr_2[i,0], nuc_stampe_data_arr[i,0]/nuc_stampe_data_arr_2[i-1,0], nuc_stampe_data_arr[i,-1]
"""avg_factor = 0
avg_counter = 0
for i in range(len(data_arr)):
    print i+1, Li7[i+1] - Li7[i],(rad_frac[i+1] - rad_frac[i])*15.9,data_arr[i],',',dXLi7_dr[i], ',', (data_arr[i]/dXLi7_dr[i])
    if (dXLi7_dr[i] != 0 and data_arr[i] != 0):
        avg_factor = avg_factor + (data_arr[i]/dXLi7_dr[i])
        avg_counter += 1
        
    
avg_factor = avg_factor/avg_counter
print 'Number of zero-less rows: ', avg_counter
print 'Average factor = ', avg_factor
print avg_factor/6.9599
Li_grad = data_arr[:,0]
C_grad = data_arr[:,1]
N_grad = data_arr[:,2]
print data_arr[0:3,:]"""

# check graph data
#for i in range(len(nuc_dXLi7_dr_correction)): 
 #   print nuc_rad_frac[i] , nuc_dXLi7_dr_correction[i]/rad_fraction_to_Rsun , nuc_dXC12_dr_correction[i]/rad_fraction_to_Rsun , nuc_dXN14_dr_correction[i]/rad_fraction_to_Rsun 
#print nuc_burn_abund_data

with open ("mu_test_data/2_1231_focus_abund","w") as f:
    for i in range(len(nuc_burn_abund_data[:,0])): 
        nuc_burn_abund_data[i,:].tofile(f," ")
        f.write('\n')
with open ("mu_test_data/2_1231_focus_model", 'w') as f:
    for i in range(len(nuc_burn_model_data[:,0])):
        nuc_burn_model_data[i,:].tofile(f," ")
        f.write('\n')
with open ("mu_test_data/2_1231_focus_grads","w") as f:
    for i in range(len(nuc_burn_abund_data[:,0])): 
        nuc_burn_grads_data[i,:].tofile(f," ")
        f.write('\n')

with open ("mu_test_data/2_1231_focus_rad_model","w") as f:
    for i in range(len(rad_zone_model_data[:,0])): 
        rad_zone_model_data[i,:].tofile(f," ")
        f.write('\n')

     