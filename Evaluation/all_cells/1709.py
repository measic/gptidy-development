benefits_assesement = [
    'AssessBenefits1', 'AssessBenefits2', 'AssessBenefits3', 'AssessBenefits4', 'AssessBenefits5', 
    'AssessBenefits6','AssessBenefits7', 'AssessBenefits8', 'AssessBenefits9', 'AssessBenefits10', 'AssessBenefits11'
]

ff = top10_df[benefits_assesement].mode()#.groupby('Country').mean()[benefits_assesement].reset_index()
ff_p = ff.pivot_table(columns='Country')
plt.figure(figsize=(14, 8))
#for country in top_10_list:
 #   plt.plot(ff_p[country], label=country)
#plt.legend()
ff = pd.Series(index=ff.columns, data=ff.values[0])
plt.bar(ff.index, ff)
sns.despine(left=True)
plt.title('Benefits assessement comparaison', fontsize=21)
_ = plt.xticks(rotation='vertical')
#top10_df['AssessBenefits6'].mode()
