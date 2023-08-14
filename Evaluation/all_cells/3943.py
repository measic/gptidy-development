returns = dataframe.pct_change()
returns.iloc[0, :] = 0.0
display.display(returns.head())

mean_returns = returns.mean()
display.display(mean_returns)

cov_matrix = returns.cov()
display.display(cov_matrix)