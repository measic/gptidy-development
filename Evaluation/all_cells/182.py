# Monthly Revenues Across multiyear
dfm=df.pivot_table(index=[df.index.month, df.index.year]).rename_axis(['month','year'])
dfm.style.applymap(color_negative_red).apply(highlight_max).apply(highlight_min)