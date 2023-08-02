#plot the Monthly Revenue Averages to determine overall monthly comparison performance
ax=sns.lineplot(df.index.month,df['Revenue'],color='#2ecc71', label='Revenue')