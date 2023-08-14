def plot_incomesExpenses(bankdata):
    data = buildIncomesExpenses(bankdata)
    layout = go.Layout(
      xaxis = dict(title = 'Date'),
      yaxis = dict(title = 'Amount (' + CURRENCY + ')'),
      barmode = 'relative',
      title = 'Incomes and expenses'
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig, filename='barmode-relative')