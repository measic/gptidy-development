def build_index(non_empty_days, from_time, to_time):
    date_ranges = []
    for date in non_empty_days:
        yyyy, mm, dd = date.split('-')
        from_hour, from_min = from_time.split(':')
        to_hour, to_min = to_time.split(':')
        variable_def = datetime(int(yyyy), int(mm), int(dd), int(from_hour), int(from_min), 0)
        t2 = datetime(int(yyyy), int(mm), int(dd), int(to_hour), int(to_min), 0)
        date_ranges.append(pd.DataFrame({'OrganizedDateTime': pd.date_range(variable_def, t2, freq='1Min').values}))
    agg = pd.concat(date_ranges, axis=0)
    agg.index = agg['OrganizedDateTime']
    return agg