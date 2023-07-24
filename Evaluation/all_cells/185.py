# Monthly Revenues across multi-year
dfmm = df.pivot_table(index=df.index.month, aggfunc=(np.mean,np.sum, min, max))
dfmm.index.rename('month', inplace=True)
dfmm.style.applymap(color_negative_red).apply(highlight_max).apply(highlight_min)