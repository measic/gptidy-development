# Revenue per Quarter across multi-year
dfq = df.pivot_table(index=[df.index.year,df.index.quarter], 
                     aggfunc=(np.mean, np.sum, min,max)).rename_axis(['year','quarter'])

#drop the the entry for 2016 since its not a complete quarter
#dfq = dfq.iloc[0:28,:]
dfq.style.applymap(color_negative_red).apply(highlight_max).apply(highlight_min)