data2 = data_ep.dropna()
data2 = data2[['star_name',"mass","mass_error_min",
               "semi_major_axis", "semi_major_axis_error_min", "semi_major_axis_error_max","mass_error_max"]]
Data2=System(data2)
#CM_2=CenterOfMass(Data2).M_total()
#system_2 = list(data2.groupby("star_name").groups.keys())
#system
#data2 = pd.DataFrame({'system_name':system_2,'total_mass':M_total.tolist(),'center_of_Mass':CM_2.tolist()})
#data1