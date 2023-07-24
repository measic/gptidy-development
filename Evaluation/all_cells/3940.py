plt.figure(figsize=(14, 7))
for val in dataframe.columns.values:
    plt.plot(
        dataframe.index, dataframe[val], linewidth=2, alpha=0.8, label=val)
plt.title("Stocks Visualization")
plt.xlabel("Dates")
plt.ylabel("Prices ($)")
plt.legend()
plt.show()

compare_data = (dataframe / dataframe.iloc[0, :])
plt.figure(figsize=(14, 7))
for val in compare_data.columns.values:
    plt.plot(
        compare_data.index,
        compare_data[val],
        linewidth=2,
        alpha=0.8,
        label=val)
plt.title("Comparison of Stocks")
plt.xlabel("Dates")
plt.ylabel("Prices ($)")
plt.legend()
plt.show()