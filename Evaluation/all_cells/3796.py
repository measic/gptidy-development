## Ref: https://plot.ly/python/time-series/

trace_high = go.Scatter(
                x=googl.date,
                y=googl['high'],
                name = "High",
                line = dict(color = '#228B22'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=googl.date,
                y=googl['low'],
                name = "Low",
                line = dict(color = '#B22222'),
                opacity = 0.8)

data_googl = [trace_high,trace_low]

layout = {
    'title' : 'GOOGLE Stock Variation',
    'yaxis' : {'title': 'Stock Value'},
    'xaxis' : {'title' : 'Year',
               'range' : ['2014-01-01','2016-12-01'],
               'rangeselector' : dict(
                                buttons=list([
                                    dict(count=1,
                                         label='1m',
                                         step='month',
                                         stepmode='backward'),
                                    dict(count=6,
                                         label='6m',
                                         step='month',
                                         stepmode='backward'),
                                    dict(count=1,
                                         label='1y',
                                         step='year',
                                         stepmode='backward'),
                                    dict(count=5,
                                         label='5y',
                                         step='year',
                                         stepmode='backward'),                                    
                                    dict(step='all')
                                    ])
                ),
               "rangeslider" : dict(
                    visible = True
                ),
               "type" : 'date'
              }
    
}


fig = dict(data=data_googl, layout=layout)
py.iplot(fig, filename = "Variation of High and Low of Google Stock Prices")