# Plot the monthly revenues per year
ax=sns.lineplot(y='Revenue', x=df.index.month,hue=df.index.year,data=df,palette="ch:r=-.5,l=.75")