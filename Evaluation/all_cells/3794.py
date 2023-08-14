import numpy as np

aapl_close = aapl[["close"]]
dates = aapl[["date"]]

 
aapl_change = aapl_close.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.


layout = dict(title = 'Change in AAPL stock from the previous day',
               xaxis=dict(
                    title = 'Date',
                    tickcolor='#000'
                ),
                yaxis=dict(
                    title = 'Variations in stock price',
                    tickcolor='#000'
                    )
              )


# Create a trace
trace = go.Scatter(
    x = dates,
    y = aapl_change)


data_aapl_change = [trace]
fig = dict(data=data_aapl_change, layout=layout)

py.iplot(fig)