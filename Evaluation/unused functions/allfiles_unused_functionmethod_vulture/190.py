def plot_super_view(bankdata, minDate, maxDate):
    (data, min_amount, max_amount) = buildTraces(bankdata)
    piggyData = buildPiggy(bankdata)
    for piggyTrace in piggyData:
        newTrace = go.Bar(
            x = piggyTrace.x,
            y = piggyTrace.y,
            name = piggyTrace.name,
            xaxis = 'x2',
            yaxis = 'y2'
        )
        data.append(newTrace)
    layout = go.Layout(
        xaxis=dict(
            domain=[0, 0.9],
            title = 'Date',
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1 month',
                         step='month',
                         stepmode='backward'),
                    dict(count=3,
                         label='3 months',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6 months',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                        label='1 year',
                        step='year',
                        stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible = True
            ),
            type='date'
        ),
        yaxis=dict(
            range=[min_amount, max_amount],
            title = 'Amount (' + CURRENCY + ')'
        ),
        xaxis2=dict(
            domain=[0.9, 1]
        ),
        yaxis2=dict(
            anchor='x2',
            range=[min_amount, max_amount],
            showticklabels=False
        ),
        title = 'Super view ' + minDate.strftime("%m/%d/%Y") + ' - ' + maxDate.strftime("%m/%d/%Y"),
        barmode='stack'
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig, filename='side-by-side-subplot')