e_series = e_series_2019.set_index(pd.DatetimeIndex(e_series_2019['ts'], name='ut').tz_localize('MST').tz_convert(None)).drop(columns=['ts'])
e_series.head()