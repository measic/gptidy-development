def plot_general(bankdata, minDate, maxDate):
    (data, _, _) = buildTraces(bankdata)
    layout = go.Layout(title = 'Saldo ' + minDate.strftime("%m/%d/%Y") + ' - ' + maxDate.strftime("%m/%d/%Y"),
                  xaxis = dict(title = 'Fecha'),
                  yaxis = dict(title = 'Saldo (' + CURRENCY + ')'),
                  showlegend = True
    )

    fig = dict(data=data, layout=layout)
    py.offline.iplot(fig, filename='styled-line')