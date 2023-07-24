fixed = data.drop(columns=['ut']).set_index(pd.DatetimeIndex(data['time'], name='ut'))
fixed.head()