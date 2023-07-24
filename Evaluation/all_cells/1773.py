view_scatter = go.Scatter3d(
    x=trace_viewing_x,
    y=trace_viewing_y,
    z=trace_viewing_z,
    mode='markers',
    marker=dict(
        size=12,
        line=dict(
            color='rgba(217, 217, 217, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)

layout = go.Layout(
    title='Viewing places',
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
fig = go.Figure(data=[view_scatter], layout=layout)
iplot(fig, filename='viewing')