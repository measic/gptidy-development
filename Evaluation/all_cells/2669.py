%matplotlib inline
from matplotlib import pyplot as plt
from matplotlib import colors as clr
import numpy as np
import sys
import re
import fileinput
#from mpl_toolkits.mplot3d import Axes3D

temp_abund_data = []
temp_model_data = []
temp_grad_data = []
temp_test_data = []

y_param_list = []
y_param_names = []
oldstr = ['0-','1-','2-','3-','4-','5-','6-','7-','8-','9-']
newstr = ['0 -','1 -','2 -','3 -','4 -','5 -','6 -','7 -','8 -','9 -']

# function to plot all dA/dr vs radius for species parameter A
def radius_vs_rad_gradient_plot(ax, rad_frac_var, dXi_dr,xlim_low, xlim_up, species,legend_tf):
    ax.axhline(y=0.0, color='m', linestyle='--')
    ax.plot(rad_frac_var*(first_line_R), dXi_dr, 'g')
    ax.set_xlabel('Radius / $R_{\odot}$')
    ax.set_ylabel('d$X_{'+species+'}$/dr / $(M_{'+species+'}/M_{layer}) R_{\odot}$ $^{-1}$')
    
    if legend_tf:
        plt.legend(loc='upper left', bbox_to_anchor=(0.5, 0.5))

    #add fractional radius label to plot
    frac_x = ax.twiny()
    frac_x.set_xlim(min(rad_frac_var),(xlim_up/first_line_R))
    frac_x.set_xlabel('Fractional radius')
    ax.set_xlim([xlim_low, xlim_up])
    #stam_graf0.set_ylim([-0.0003, 0.001])
    #plt.show()
    ax.set_title(species+' abundance gradient for log$(L/L_{\odot})$ = 2.1231\n 1M_sun, Z=Z_sun with diffusion', y=1.15)
    
# function to change file into space-separated float fields and parameterise the data using this new format
# line in 'with open' bit is type 'str'

# create a function to get data in radiative layers of star (between core and convective envelope)
bound_inds = []

def data_read_CE(f,xfunc):
    missed_line_inds = []
    temp_data = []
    temp_rad_zone_data = []
    check = 0
    #number of lines to cut = number of line containing 'convective shell' label - (2 + any additional string lines)
    lines_cut = 0
    for line in f:
        for i in range(len(oldstr)):
            line = line.replace(oldstr[i],newstr[i])
        check = check + 1
        for x in range(4,1,-1):
            line = line.replace((x*' '),' ')
        line = line.replace('D','E')
        match_ast = re.search('[**]', line)
        match_inf = re.search('Infinity',line)
        match_core = re.search('CORE',line)
        match_env = re.search('INTERNO SHELL CONVETTIVA',line)
        if match_core or match_env:
            bound_inds.append(check)
            print 'boundary index = ',check
        elif match_ast or match_inf or (line.strip()==''):
            missed_line_inds.append(check)
            continue
        else:
            file_data = np.array([float(parameter) for parameter in line.strip().split(' ')])
            temp_data.append(file_data)
    out_all_data = np.array(temp_data)
    if (out_all_data[-1,0] == 0):
        print 'Data ends with mass = 0 line - cutting this line',out_all_data.shape
        out_all_data = out_all_data[0:-1]
        print 'Fixed data shape',out_all_data.shape
        print 'Fixed data last line',out_all_data[-1,:]
    print 'Missed line indices: ',missed_line_inds
    
    if (xfunc == 'model'):
        print 'extracting radiative zone data'
        for i in missed_line_inds:
            print i
            if (bound_inds[0] < i < bound_inds[-1]):
                lines_cut = lines_cut + 1
        print 'lines cut: ',lines_cut
        for j in range(len(out_all_data[:,-1])):
            #if (j - (j-1) != 1):
            #    print j,j-1
            if (bound_inds[0] <= out_all_data[j,-1] <= (bound_inds[-1] - (lines_cut+2))):
                temp_rad_zone_data.append(out_all_data[j,:])
        out_rad_zone_data = np.array(temp_rad_zone_data)
    
        print 'Bounds: ',out_all_data[bound_inds[0],-1],out_all_data[bound_inds[-1],-1]
        print out_rad_zone_data.shape,', theoretical range: ',(bound_inds[-1]-bound_inds[0]-2)
    else:
        print 'not model file'
        out_rad_zone_data = np.array(temp_rad_zone_data)
    
    print 'Total dataset: ',out_all_data.shape,'Last mesh point: ', out_all_data[-1,-1]
    return out_all_data,out_rad_zone_data
            

#def get_abund_params(param_list,dataset):

def data_focus(focus_parameter,focus_value,file_data):
    focus_data = []
    check = 0
    for i in range(len(focus_parameter)):
        if (focus_parameter[i] > focus_value):
            #print type(eps_nuclear[i])
            focus_data.append(file_data[i,:])
            check = check + 1
        else:
            continue
    print check
    return np.array(focus_data)

def focus_sync(first_file_focussed,second_file_data):
    second_file_focussed = []
    check = 0
    for i in range(len(second_file_data[:,0])):
        if (second_file_data[i,-1] in first_file_focussed[:,-1]):
            second_file_focussed.append(second_file_data[i,:])
            check = check + 1
        else:
            continue
    print check
    return np.array(second_file_focussed)

# end of functions
print 'modules & functions done'