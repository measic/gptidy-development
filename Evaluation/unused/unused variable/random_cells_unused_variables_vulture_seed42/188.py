#plot the monthly revenues per year
ax=sns.boxplot(y='Revenue', x=df.index.quarter,data=df,color='#2ecc71')