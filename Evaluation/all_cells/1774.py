traces = []
list_img = read_img_list()


for i, row in df_viewing[150:155].iterrows():
    illum_x, illum_y, illum_z = polar_to_euclidean(row['illum_theta'],row['illum_phi'])
    view_x, view_y, view_z = polar_to_euclidean(row['view_theta'],row['view_phi'])

    line_x = [illum_x, illum_x, 0, view_x]
    line_y = [illum_y, illum_y, 0, view_y]
    line_z = [illum_z-0.05, illum_z, 0, view_z]
    
    # plotting line
    line_scatter = go.Scatter3d(
        x=line_x,
        y=line_y,
        z=line_z,
        name=os.path.basename(list_img[i])
    )
    
    traces.append(line_scatter)

    
layout = go.Layout(
    title='Illumination and viewing pairs',
    autosize=True,
    width=900,
    height=800,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)

fig = go.Figure(data=traces, layout=layout)
iplot(fig, filename='elevations-3d-surface')