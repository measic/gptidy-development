def plot_profit(bankdata):
    data = buildProfit(bankdata)
    layout = go.Layout(
        title = 'Monthly profit',
        barmode ='group',
        xaxis = dict(title = 'Date'),
        yaxis = dict(title = 'Amount (' + CURRENCY + ')')
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig, filename='grouped-bar')