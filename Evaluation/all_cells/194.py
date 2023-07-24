dfyy = df.pivot_table(index=df.index.year, aggfunc=(np.mean,np.sum, min, max)).rename_axis('year')
dfyy.style.applymap(color_negative_red).apply(highlight_max).apply(highlight_min)