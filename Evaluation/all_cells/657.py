# Let's add the cantons to our dataframe !
p3_grant_cantons = pd.concat([p3_grant_export_data_reindex, canton_longname_series, canton_shortname_series], axis=1)
p3_grant_cantons.columns.get_value
p3_grant_cantons