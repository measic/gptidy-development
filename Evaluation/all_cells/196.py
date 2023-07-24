#plot the yearly avg revenues to determine yearly overall performance
ax=sns.lineplot(df.index.year,df['Revenue'],color='#2ecc71', label='Revenue')