# window the data using your windowing function
window_size = 7
X,y = window_transform_series(series = dataset,window_size = window_size)