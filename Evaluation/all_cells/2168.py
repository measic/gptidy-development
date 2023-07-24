import seaborn as sns

freqs = [score[1] for score in comm_enrich_scores]

sns.set(color_codes=True)
sns.kdeplot(freqs, shade=True)