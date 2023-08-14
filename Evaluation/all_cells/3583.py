"""
2) Medelvärdet av EK för varje parameter beräknas för varje år.
"""
by_year = by_date.groupby('YEAR').mean_ek_value.agg(['count', 'min', 'max', 'mean']).reset_index()
by_year.rename(columns={'mean':'mean_ek_value', 'count': 'number_of_dates'}, inplace=True)
by_year['all_ok'] = True
by_year.loc[by_year['number_of_dates'] < 1, 'all_ok'] = False
# by_year.to_csv(self.paths['results'] +'/' + self.name + water_body + 'by_year.txt', sep='\t')
by_year