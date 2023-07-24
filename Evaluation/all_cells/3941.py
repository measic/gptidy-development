returns = dataframe.pct_change()  # Caluculates daily returns
returns.iloc[0, :] = 0  # replaces nan with 0.00
display.display(returns.head(10))

plt.figure(figsize=(14, 7))
for val in returns.columns.values:
    plt.plot(returns.index, returns[val], linewidth=2, alpha=0.8, label=val)

plt.title("Daily Returns of Portfolios")
plt.ylabel("Returns")
plt.xlabel("Dates")
plt.legend()
plt.show()