earlybirds = df[np.logical_or(np.logical_or(df['WakeTime'] == 'Between 7:01 - 8:00 AM', df['WakeTime'] == 'Between 6:01 - 7:00 AM'), df['WakeTime'] == 'Between 5:00 - 6:00 AM')] 

plt.figure(figsize=(14, 8))
sns.countplot(data=earlybirds, x='Country', hue='WakeTime', palette='Paired', order=earlybirds['Country'].value_counts()[:10].index)
sns.despine(left=True)
plt.xticks(rotation='vertical')
