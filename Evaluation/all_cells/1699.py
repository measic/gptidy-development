job_assesement = [
    'AssessJob1', 'AssessJob2', 'AssessJob3', 'AssessJob4', 'AssessJob5', 
    'AssessJob6','AssessJob7', 'AssessJob8', 'AssessJob9', 'AssessJob10'
]
ff = top10_df.groupby('Country').mean()[job_assesement].reset_index()
ff_p = ff.pivot_table(columns='Country')
plt.figure(figsize=(14, 8))
for country in top_10_list:
    plt.plot(ff_p[country], label=country)
plt.legend()
sns.despine(left=True)
plt.title('Job assessement comparaison by country', fontsize=21)