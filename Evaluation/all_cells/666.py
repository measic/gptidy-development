movies = movies.set_index('Reviewers')
revavg = movies.mean(axis=1).round(decimals=0)

movieavg = movies.mean().round(decimals=0)

revavg