by_date = df.groupby(['SDATE', 'YEAR'],).ek_value.agg(['count', 'min', 'max', 'mean']).reset_index()
# by_date.to_csv(self.paths['results'] +'/' + self.name + water_body +'by_occation.txt', sep='\t')
by_date.rename(columns={'mean':'mean_ek_value', 'count': 'number_of_values'}, inplace=True) # Cant use "mean" below
by_date