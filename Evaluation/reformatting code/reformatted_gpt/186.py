def plot_piggy(bankdata):
    data = buildPiggy(bankdata)
    layout = go.Layout(
        title='Saving',
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig, filename='stacked-bar')