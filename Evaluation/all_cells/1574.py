# merge the datasets
result = pd.merge(Pixel, E01, left_index=True, right_index=True)