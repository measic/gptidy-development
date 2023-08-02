def function_def(data):
    final_variances = []
    for d in data:
        variances = []
        skewnesses = []
        kurtosises = []
        stats = []
        for channel in d:
            var = channel.var()
            variances.append(var)
            skewness = skew(channel, axis=0)
            skewnesses.append(skewness)
            kurt = kurtosis(channel)
            kurtosises.append(kurt)
        final_variances.append([variances, skewnesses, kurtosises])
    return np.array(final_variances)