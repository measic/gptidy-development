target = 'Col174'
input_features = [ft for ft in data.columns.values if ft != target]
storage = DefaultResultStorage(input_features)
correlation = IncrementalCorrelation(data, target, storage, iterations = 10, alpha = 0.1, drop_discrete = False)