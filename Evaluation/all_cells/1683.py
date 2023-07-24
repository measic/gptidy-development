top_10_list = list(df['Country'].value_counts()[:10].index)
def st_not(row):
    if 'dissatisfied' in row:
        return 'Dissatisfied'
    return 'Satisfied'

df['sat_or_not'] = df['JobSatisfaction'].dropna().map(st_not)
#sat = df[np.logical_or(np.logical_or(df['JobSatisfaction'] == 'Moderately satisfied', df['JobSatisfaction'] == 'Extremely satisfied'), df['JobSatisfaction'] == 'Slightly satisfied')]
top10_df = df.where(df['Country'].isin(top_10_list))
sat_count = pd.DataFrame()
names = []
sat = []
disat = []
for name, group in top10_df.groupby('Country'):
    names.append(name)
    country_count = group['sat_or_not'].value_counts()
    sat.append(country_count['Satisfied'])
    
    #sat_count['Satisfied'] = country_count['Satisfied']
    #sat_count['Dissatisfied'] = country_count['Dissatisfied']
sat_count['Country'] = names
    #plt.figure(figsize=(14, 8))
#plt.plot(sat_count)
#sns.countplot(data=df, x='Country', hue='sat_or_not', palette='Paired', order=df['Country'].value_counts()[:10].index)
#sns.despine(left=True)
#plt.xticks(rotation='vertical')
sat_count