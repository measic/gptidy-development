# Convert HH:MM:SS to total seconds

def time_convert(x):
    if x == "-":
        return None
    else:
        times = x.split(':')
        return (3600*int(times[0])+60*int(times[1]))+int(times[2])


boston_join['5K Duration'] = boston_join['5K'].apply(time_convert)
boston_join['10K Duration'] = boston_join['10K'].apply(time_convert)
boston_join['15K Duration'] = boston_join['15K'].apply(time_convert)
boston_join['20K Duration'] = boston_join['20K'].apply(time_convert)
boston_join['Half Duration'] = boston_join['Half'].apply(time_convert)
boston_join['25K Duration'] = boston_join['25K'].apply(time_convert)
boston_join['30K Duration'] = boston_join['30K'].apply(time_convert)
boston_join['35K Duration'] = boston_join['35K'].apply(time_convert)
boston_join['40K Duration'] = boston_join['40K'].apply(time_convert)
boston_join['Official Time Duration'] = boston_join['Official Time'].apply(time_convert)

# Drop rows with null values

boston_join.dropna(inplace=True,subset=['Bib','Age','5K Duration','10K Duration','15K Duration','20K Duration', 'Half Duration', '25K Duration','30K Duration','35K Duration','40K Duration','Official Time Duration', 'Temp (F)'])

boston_clean=boston_join[['Bib','Age','5K Duration','10K Duration','15K Duration','20K Duration', 'Half Duration', '25K Duration','30K Duration','35K Duration','40K Duration','Official Time Duration', 'Temp (F)', 'F', 'M']]

# boston_clean[['Bib','5K Duration','10K Duration','15K Duration','20K Duration','Half Duration', '25K Duration','30K Duration','Official Time Duration']]

boston_clean.columns