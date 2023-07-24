print("-" * 37)
print("    Histogram Analysis of Tickers")
print("-" * 37)


def hisogram_stats(val):
    print("      Mean of " + val + " : {:.5f}".format(returns[val].mean()))
    print("      Std of " + val + " : {:.5f}".format(returns[val].std()))
    print("      Kurtosis of " + val +
          " : {:.5f}".format(returns[val].kurtosis()))
    print("-" * 37)


for val in returns.columns:
    hisogram_stats(val=val)

    plt.figure(figsize=(10, 5))
    returns[val].plot.hist(label=val, bins=35, color="g")

    plt.axvline(returns[val].mean(), color="w", linewidth=2, linestyle="--")
    plt.axvline(returns[val].std(), color="b", linewidth=2, linestyle="--")
    plt.axvline(-returns[val].std(), color="b", linewidth=2, linestyle="--")

    plt.title(val + " Histogram")
    plt.legend()
plt.show()