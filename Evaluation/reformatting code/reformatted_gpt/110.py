# Quarterly Revenues across multi-year
dfqq = df.pivot_table(index=df.index.quarter, aggfunc=(np.mean, np.sum, min, max)).rename_axis('quarter')
dfqq.style.applymap(color_negative_red).apply(highlight_max).apply(highlight_min)