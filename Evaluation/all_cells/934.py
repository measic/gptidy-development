def difference(dataset,interval=1):
    diff=list()
    for i in range(interval, len(dataset)):
        value=dataset[i]-dataset[i-interval] # calcualting row vs row(-1) differnce
        diff.append(value)
    return pd.Series(diff)

# Not sure what this differencing does as of right now