"""
3) Medelvärdet av EK för varje parameter och vattenförekomst (beräknas för minst
en treårsperiod)
"""
by_period = by_year[['mean_ek_value']].describe()#.agg(['count', 'min', 'max', 'mean'])
by_period = by_period.transpose()
#by_period#.loc['mean', 'mean_ek_value']
#
#by_period['count'].get_value('mean_ek_value')
by_period['all_ok']  = True
if by_period['count'].get_value('mean_ek_value') < 3:
    by_period['all_ok'] = False

by_period