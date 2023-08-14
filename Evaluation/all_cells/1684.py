plt.figure(figsize=(14, 12))
df_top10 = df.where(df['Country'].isin(top_10_list))

sns.boxplot(data=df_top10, x='ConvertedSalary', y='Country', palette='Paired')
plt.title('Salary Distribution in the Top 10 Countries', fontsize=16)
sns.despine(left=True)