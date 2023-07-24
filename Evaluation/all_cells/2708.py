for name, df in fixed_names.items():
    if name == 'Contents':
        continue
    df = df[df['PrecinctName'].apply(lambda x: str(x).startswith('Pct '))]
    df.columns = [to_appropriate_column_name(x.replace('(%)', 'Percent')) for x in df.columns]
    df.to_csv(os.path.join(PATH, 'derived_data', '{}.csv'.format(name)), encoding='utf-8', index=False)
    #####
    agg_methods = {
    'precincts': 'min',
    'registration': 'min'
    }
    no_agg = ['OBJECTID', 'precinctname', 'reportingtype', 'precinctid', 'turnout_percent']
    grouped_df = df.groupby('precinctid').agg({x: agg_methods.get(x, 'sum') for x in df.columns if x not in no_agg})
    grouped_df.to_csv(os.path.join(PATH, 'derived_data', '{}.csv'.format('precinct_summary_' + name)), encoding='utf-8', index=True)