# Plot the revenues for different months and years
ax=sns.lineplot(y='Revenue', x=df.index.year,hue=df.index.month,data=df,palette="ch:r=-.5,l=.75", legend=False)