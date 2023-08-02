def plot_incomesExpensesProfits(bankdata):
    data = buildIncomesExpenses(bankdata)
    
    dataProfit = buildProfit(bankdata)
    
    # Profits per bank
    for barProfit in dataProfit:
        trace_profit = go.Scatter(
            x = barProfit.x,
            y = barProfit.y,
            name = barProfit.name,
            mode = 'markers'
        )
        data.append(trace_profit)
    
    # Total profits
    totalProfits = {}
    for barProfit in dataProfit:
        for date, value in zip(barProfit.x, barProfit.y):
            key = date.strftime("%m/%Y")
            if key in totalProfits:
                totalProfits[key] += value
            else:
                totalProfits[key] = value
    
    xs = []
    ys = []
    for key, value in totalProfits.items():
        xs.append(dt.datetime.strptime(key, '%m/%Y').date())
        ys.append(value)
    
    trace_profit = go.Scatter(
        x = xs,
        y = ys,
        name = 'Profit',
        mode = 'markers',
        marker = dict(
            size = 10,
            line = dict(
                width = 2,
            )
        )
    )
    data.append(trace_profit)
    
    layout = go.Layout(
      xaxis = dict(
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
      yaxis = dict(title = 'Amount (' + CURRENCY + ')'),
      barmode = 'relative',
      title = 'Incomes, expenses and profit'
    )
    fig = go.Figure(data=data, layout=layout)
    py.offline.iplot(fig, filename='barmode-relative')