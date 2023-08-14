trace_illum_x = []
trace_illum_y = []
trace_illum_z = []

trace_viewing_x = []
trace_viewing_y = []
trace_viewing_z = []

for i, row in df_viewing.iterrows():
    illum_x, illum_y, illum_z = polar_to_euclidean(row['illum_theta'],row['illum_phi'])
    view_x, view_y, view_z = polar_to_euclidean(row['view_theta'],row['view_phi'])
    
    line_x = [illum_x, 0, view_x]
    line_y = [illum_y, 0, view_y]
    line_z = [illum_z, 0, view_z]
    
    trace_illum_x.append(illum_x)
    trace_illum_y.append(illum_y)
    trace_illum_z.append(illum_z)
    
    trace_viewing_x.append(view_x)
    trace_viewing_y.append(view_y)
    trace_viewing_z.append(view_z)